import sys

def trace_lines(frame, event, arg):
    # We are only interested in 'line' events
    if event == 'line':
        # Get the function name, line number, and the source code of that line
        code = frame.f_code
        func_name = code.co_name
        line_no = frame.f_lineno
        
        # To get the actual line of code, you need to read the file
        # (This is a simplified example)
        print(f"Executing: Function '{func_name}', Line {line_no}")
        
    return trace_lines # You must return the tracer function to keep tracing

# --- A simple program to trace ---
def greet(name):
    print(f"Hello, {name}")
    if len(name) > 5:
        print("You have a long name!")
    else:
        print("Your name is short.")

def run_program():
    x = 10
    greet("World")
    greet("Christopher")
    y = 20

# --- Start tracing and run the program ---
sys.settrace(trace_lines)
run_program()
sys.settrace(None) # Stop tracing