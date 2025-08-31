from flask import Flask, request, jsonify
from flask_cors import CORS
import ast
import networkx as nx
import sys
import threading
from queue import Queue
import json

# --- AST and Graph Generation (from HoloDeck5.py) ---
def generate_3d_network(code_string):
    try:
        tree = ast.parse(code_string)
    except SyntaxError as e:
        # Re-raise with more context for the frontend
        raise SyntaxError(f"Error parsing Python code on line {e.lineno}: {e.text.strip()}\n{e.msg}")

    graph = nx.DiGraph()
    code_lines = code_string.splitlines()

    # Add all lines as nodes first, without a type
    for i, line in enumerate(code_lines):
        graph.add_node(i + 1, code=line.strip())

    class NetworkVisitor(ast.NodeVisitor):
        def __init__(self, graph):
            self.graph = graph
            self.line_map = {i + 1: line.strip() for i, line in enumerate(code_lines)}
            self.node_types = {}
            self.type_priority = {
                'definition': 6,
                'control_flow': 5,
                'function_call': 4,
                'operation': 3,
                'data_change': 2,
                'literal': 1
            }

        def visit(self, node):
            if hasattr(node, 'lineno'):
                line_no = node.lineno
                node_type = self.get_node_type(node)
                if node_type:
                    current_priority = self.type_priority.get(self.node_types.get(line_no), 0)
                    new_priority = self.type_priority.get(node_type, 0)
                    if new_priority > current_priority:
                        self.node_types[line_no] = node_type
            self.generic_visit(node)

        def visit_body(self, body_nodes, parent_lineno):
            prev_lineno = parent_lineno
            for node in body_nodes:
                if not hasattr(node, 'lineno'): continue
                # self.visit(node) # This is already called by generic_visit in the main traversal
                # Ensure both source and target nodes exist before adding an edge
                if self.graph.has_node(prev_lineno) and self.graph.has_node(node.lineno):
                    self.graph.add_edge(prev_lineno, node.lineno)
                prev_lineno = node.lineno
            return prev_lineno

        def get_node_type(self, node):
            """Categorizes an AST node into one of our 6 types."""
            if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Import, ast.ImportFrom)):
                return 'definition'
            if isinstance(node, (ast.If, ast.For, ast.While, ast.Try, ast.Return, ast.Break, ast.Continue)):
                return 'control_flow'
            if isinstance(node, ast.Call):
                return 'function_call'
            if isinstance(node, (ast.Assign, ast.AugAssign, ast.List, ast.Dict, ast.Tuple, ast.Set)):
                return 'data_change'
            if isinstance(node, (ast.BinOp, ast.Compare, ast.BoolOp, ast.UnaryOp)):
                return 'operation'
            if isinstance(node, ast.Constant):
                return 'literal'
            return None

        def visit_FunctionDef(self, node):
            self.visit_body(node.body, node.lineno)
            self.generic_visit(node)

        def visit_For(self, node):
            last_body_node_lineno = self.visit_body(node.body, node.lineno)
            # Edge from end of loop back to the start
            if self.graph.has_node(last_body_node_lineno) and self.graph.has_node(node.lineno):
                 self.graph.add_edge(last_body_node_lineno, node.lineno)
            self.generic_visit(node)

        def visit_While(self, node):
            last_body_node_lineno = self.visit_body(node.body, node.lineno)
            # Edge from end of loop back to the start
            if self.graph.has_node(last_body_node_lineno) and self.graph.has_node(node.lineno):
                 self.graph.add_edge(last_body_node_lineno, node.lineno)
            self.generic_visit(node)

        def visit_If(self, node):
            self.visit_body(node.body, node.lineno)
            if node.orelse:
                self.visit_body(node.orelse, node.lineno)
            self.generic_visit(node)

    visitor = NetworkVisitor(graph)
    visitor.visit(tree)
    visitor.visit_body(tree.body, 0) # Explicitly visit the top-level body

    # Update the nodes with the determined type
    for line_no, node_type in visitor.node_types.items():
        if line_no in graph.nodes:
            graph.nodes[line_no]['type'] = node_type

    # Use a 3D spring layout
    pos_3d = nx.spring_layout(graph, dim=3, seed=42, k=0.5, iterations=50)
    return graph, pos_3d

# --- Execution Tracing (from HoloDeck5.py) ---
class ExecutionTracer:
    def __init__(self, code, queue):
        self.code = code
        self.queue = queue
        self.executed_lines = set()

    def trace_function(self, frame, event, arg):
        # We only care about the 'line' event
        if event == 'line':
            lineno = frame.f_lineno
            # To avoid infinite loops in tracing, limit to a reasonable number of total trace steps
            if len(self.executed_lines) < 200:
                self.queue.put(lineno)
                self.executed_lines.add(lineno)
        return self.trace_function

    def run_code(self):
        # Set the trace function for the current thread
        sys.settrace(self.trace_function)
        try:
            # Execute the user's code in a restricted scope
            exec(self.code, {"__name__": "__main__"})
        except Exception as e:
            print(f"Error during traced execution: {e}")
        finally:
            # Always remove the trace function
            sys.settrace(None)
            self.queue.put(None) # Signal that tracing is finished

# --- Flask App ---
app = Flask(__name__)
CORS(app) # Enable Cross-Origin Resource Sharing for local development

@app.route('/api/generate_graph', methods=['POST'])
def generate_graph_endpoint():
    data = request.get_json()
    if not data or 'code' not in data:
        return jsonify({"error": "Invalid request. 'code' field is required."}),
    
    code = data['code']

    try:
        # 1. Generate Graph
        graph, pos = generate_3d_network(code)

        # 2. Format Graph Data for Frontend
        nodes = [
            {
                "id": int(node_id),
                "code": graph.nodes[node_id].get('code', ''),
                "type": graph.nodes[node_id].get('type', 'data_change'), # Pass the type
                # Scale positions to fit the frontend's desired [-10, 10] cube
                "position": [p * 10 for p in pos[node_id]]
            }
            for node_id in graph.nodes()
        ]

        edges = [
            {"source": int(source), "target": int(target)}
            for source, target in graph.edges()
        ]

        # 3. Generate Execution Trace
        trace_queue = Queue()
        tracer = ExecutionTracer(code, trace_queue)
        # Running the trace in a separate thread to avoid blocking
        trace_thread = threading.Thread(target=tracer.run_code, daemon=True)
        trace_thread.start()
        trace_thread.join(timeout=5) # Add a timeout to prevent hangs from infinite loops

        trace = []
        while not trace_queue.empty():
            line_no = trace_queue.get()
            if line_no is not None:
                trace.append(line_no)

        # 4. Combine and send the response
        response_data = {
            "graph": {"nodes": nodes, "edges": edges},
            "trace": trace
        }
        return jsonify(response_data)

    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": str(e)}),

if __name__ == '__main__':
    # Add instructions to install dependencies
    try:
        import networkx
        import flask
        import flask_cors
        import numpy
    except ImportError:
        print("\n---")
        print("One or more required Python packages are not installed.")
        print("Please run the following command to install them:")
        print("pip install Flask networkx Flask-Cors numpy")
        print("---\n")
        sys.exit(1)

    print("Starting Python Holodeck server at http://127.0.0.1:5001")
    app.run(host='0.0.0.0', port=5001, debug=False)
