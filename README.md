# maze_generator_solver



├── a_maze_ing.py          # Main entry point (Mandatory Name) [cite: 113]
├── Makefile               # Task automation [cite: 83]
├── config.txt             # Default configuration [cite: 127]
├── .gitignore             # Exclude __pycache__, etc. [cite: 100]
├── README.md              # Project documentation [cite: 205]
└── src/
    └── maze_logic/        # Your reusable module 
        ├── __init__.py    # Makes the directory a package
        ├── parser.py      # Logic for reading config.txt 
        ├── generator.py   # The MazeGenerator class 
        ├── solver.py      # Pathfinding logic (DFS/BFS) 
        └── renderer.py    # Terminal/MLX display logic 