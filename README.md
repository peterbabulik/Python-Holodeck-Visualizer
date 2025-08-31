# 🚀 Python Holodeck Visualizer

### An interactive 3D journey through the universe of your code.

<div align="center">
  
  <br/>
  *Visualize not just the structure of your code, but the story of its execution.*
</div>

## About The Project

Have you ever looked at a complex Python script and wished you could see it as more than just a wall of text? The Python Holodeck Visualizer transforms that text into an immersive, explorable 3D universe.

This project bridges the gap between abstract syntax and tangible structure. By uploading any Python script, you can generate an interactive 3D graph of its control flow. More powerfully, you can then watch a real-time trace of the code's execution, following the "information flow" as it travels from node to node like a spaceship navigating a star chart.

This tool was built to change how we learn, debug, and appreciate code, making the invisible logic of programming visible and beautiful.

<div align="center">
  
  <br/>
  *The Holodeck is powerful enough to visualize its own complex source code.*
</div>

## ✨ Key Features

*   **🌐 3D Code Visualization:** Automatically parses Python code into a 3D control flow graph using `ast` and `networkx`.
*   **🛰️ Real-time Execution Tracing:** Leverages `sys.settrace` to capture the execution of your code line-by-line and animates the path through the 3D graph.
*   **🎬 Cinematic "Spaceship" Camera:** During execution, an automatic camera gracefully flies and rotates to follow the "information flow," creating an intuitive journey through your program's logic.
*   **🎮 Interactive Camera Controls:** When not tracing, take full control with multiple camera modes:
    *   **Orbit:** Left-click and drag to rotate around the entire code structure.
    *   **Fly:** Right-click and use WASDQE for first-person "spaceship" exploration.
    *   **Static/Observe:** Pan the view with a locked orientation or watch the execution flow from a fixed vantage point.
*   **⚙️ Execution Control:** An interactive UI allows you to start the trace and control the execution speed (100%, 75%, 50%, 25%).
*   **💻 Live Console Output:** An on-screen execution log displays the real-time `print()` output of your script as it runs.
*   **⬆️ Upload and Go:** A clean, modern web interface built with **React** and **Three.js** allows you to upload any `.py` file and start visualizing instantly.

## 🛠️ How It Works: The Tech Stack

The Holodeck operates on a modern client-server architecture, leveraging the best of both Python and JavaScript ecosystems.

### Backend (The "Brain")

*   **Server:** **Flask** provides a lightweight and robust API endpoint.
*   **Code Parsing:** Python's built-in **`ast`** module parses the source code into an Abstract Syntax Tree.
*   **Graph Generation:** **`NetworkX`** is used to build a directed graph from the AST, representing the code's logical structure.
*   **3D Layout:** `NetworkX`'s force-directed spring layout algorithm calculates the optimal `(x, y, z)` position for each node in 3D space.
*   **Execution Tracing:** The magic is in the **`sys.settrace`** function, which hooks into the Python interpreter to capture each line of execution in a separate thread.

### Frontend (The "Holodeck")

*   **Framework:** **React** with **TypeScript** for a modern, type-safe user interface.
*   **3D Rendering:** **Three.js** and **`@react-three/fiber`** are used to create the high-performance WebGL scene, rendering the nodes, connections, and camera.
*   **Helpers & Controls:** **`@react-three/drei`** provides ready-made helpers for text, camera controls, and more.
*   **State Management:** **`Zustand`** manages the application's global state (e.g., `loading`, `tracing`, `error`).
*   **Styling:** **Tailwind CSS** is used for a clean, responsive design.

## 🚀 Running Locally

This project is fully self-contained. Follow these steps to launch your own Holodeck instance.

**Prerequisites:**
*   Node.js (v18 or higher)
*   Python 3

1.  **Clone the Repository**
```bash
git clone https://github.com/peterbabulik/Python-Holodeck-Visualizer.git
cd python-holodeck-visualizer
```

**2. Install Dependencies**

*   **Frontend (Node.js):**
    ```bash
    npm install
    ```
*   **Backend (Python):**
    *It's highly recommended to use a virtual environment.*
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install Flask networkx Flask-Cors
    ```

**3. Launch the Application**
The `dev` script conveniently starts both the Vite frontend and Flask backend servers at the same time.

```bash
npm run dev
```

Your browser should automatically open to `http://localhost:5173`. You're ready to fly