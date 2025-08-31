### The 6 Core Node Types for Color Diversification

Here is a proposed system, moving from the largest structures down to the most basic elements. Each category has a suggested color and a rationale for why it fits.

---

**1. Program Structure & Definitions (Majestic Purple)** `🟣`

These nodes define the architecture and dependencies of your program. They are the foundational pillars and entry points.

*   **What it includes:** `def` (Function Definitions), `class` (Class Definitions), `import` statements.
*   **AST Nodes:** `ast.FunctionDef`, `ast.ClassDef`, `ast.Import`, `ast.ImportFrom`.
*   **Why Purple?** Purple often signifies structure, royalty, and high importance. These nodes are the "scaffolding" of your code universe.

---

**2. Control Flow (Conditional Amber)** `🟠`

These nodes make decisions and direct the path of execution. They are the "forks in the road" and the "gateways" of your information flow.

*   **What it includes:** `if`, `elif`, `else`, `for`, `while`, `try`/`except`, `return`, `break`, `continue`.
*   **AST Nodes:** `ast.If`, `ast.For`, `ast.While`, `ast.Try`, `ast.Return`, `ast.Break`, `ast.Continue`.
*   **Why Amber/Orange?** This is the color of caution and decision, like a traffic light. It instantly tells the user, "Pay attention, the path might change here."

---

**3. Data & State Changes (Creative Cyan)** `🔵`

These nodes are responsible for creating, storing, or modifying data. They represent the state of your program. This is where your "variables" idea fits perfectly.

*   **What it includes:** Variable assignments (`x = 10`), augmented assignments (`x += 1`), and the creation of data structures (`my_list = []`).
*   **AST Nodes:** `ast.Assign`, `ast.AugAssign`, `ast.List`, `ast.Dict`, `ast.Tuple`, `ast.Set`.
*   **Why Cyan/Blue?** Blue is a calm, constructive color. It feels like building or creating something tangible (data). This can be the default color you're already using.

---

**4. Function Calls & I/O (Action-Oriented Green)** `🟢`

These nodes *execute* an action. They are the "verbs" of your program, where something actively happens, especially interaction with the outside world (like printing to the screen).

*   **What it includes:** Any function call, especially `print()`, `input()`, file operations (`open()`), or calls to your own functions.
*   **AST Nodes:** `ast.Call` (this is the most important one).
*   **Why Green?** Green often means "go," action, and execution. It clearly signals that a self-contained process is being kicked off.

---

**5. Operations & Expressions (Logical Red)** `🔴`

These nodes perform a calculation or comparison that results in a new value. They are the "logic units" of your code.

*   **What it includes:** Math (`+`, `-`, `*`), comparisons (`==`, `>`, `in`), and boolean logic (`and`, `or`, `not`).
*   **AST Nodes:** `ast.BinOp`, `ast.Compare`, `ast.BoolOp`, `ast.UnaryOp`.
*   **Why Red?** A bright, vibrant color like red makes these crucial logic checks stand out. It draws the eye to the core computations.

---

**6. Literals & Constants (Neutral Gray)** `⚪`

These are the raw, fundamental data values themselves. They are the "atoms" of your information space. They don't *do* anything; they just *are*.

*   **What it includes:** Numbers (`123`, `3.14`), strings (`"Hello"`), `True`, `False`, `None`.
*   **AST Nodes:** `ast.Constant`.
*   **Why Gray?** A neutral color makes them recede into the background, placing visual emphasis on the *actions* (calls, assignments, control flow) that use them.

---

### Implementation Plan

This is a two-step process: the backend needs to categorize each node, and the frontend needs to apply the color based on that category.

**Step 1: Backend (`server.py`)**

In your `generate_3d_network` function, you will modify the `NetworkVisitor` to determine the type of each node and add it to the JSON response.

```python
# In server.py, inside NetworkVisitor class

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
        # Default for anything else (like a raw expression)
        return 'data_change'

    # Modify the generic_visit or add_node method
    def generic_visit(self, node):
        if hasattr(node, 'lineno'):
            line_no = node.lineno
            if not self.graph.has_node(line_no) and line_no in self.line_map:
                node_type = self.get_node_type(node) # Get the category
                self.graph.add_node(line_no, code=self.line_map[line_no], type=node_type) # Add it here
        super().generic_visit(node)


# In your /api/generate_graph endpoint, make sure to pass the type
nodes = [
    {
        "id": int(node_id),
        "code": graph.nodes[node_id].get('code', ''),
        "type": graph.nodes[node_id].get('type', 'data_change'), # Pass the type
        "position": [p * 10 for p in pos[node_id]]
    }
    for node_id in graph.nodes()
]
```

**Step 2: Frontend (`HolodeckCanvas.tsx` or `Node.tsx`)**

In your React component that renders the nodes, you'll create a color map and use the `type` property from the API to set the color of each sphere.

```tsx
// In your component that renders the 3D scene, e.g., HolodeckCanvas.tsx

import * as THREE from 'three';

// Define your color map
const NODE_COLORS: { [key: string]: THREE.ColorRepresentation } = {
  definition: '#9b59b6',     // Purple
  control_flow: '#f39c12',  // Amber
  data_change: '#3498db',   // Cyan (Blue)
  function_call: '#2ecc71', // Green
  operation: '#e74c3c',      // Red
  literal: '#95a5a6',        // Gray
};

// ... inside your component that maps over the nodes ...

// When you create the <mesh> for each node:
const color = NODE_COLORS[node.type] || NODE_COLORS['data_change']; // Default to blue

// ...
<mesh position={node.position}>
  <sphereGeometry args={[0.5, 32, 32]} />
  <meshStandardMaterial color={color} />
</mesh>
// ...
```

By implementing this system, your Holodeck will become dramatically more insightful, allowing a user to understand the nature of a program's universe at a single glance.