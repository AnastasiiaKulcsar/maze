
# Maze Solver

A school-project script for solving maze files.

## Description

This project provides a simple command-line tool that reads a maze from a text file and solves it. You provide a maze input (for example `maze-one.txt`), and the script computes a solution path. The core file is `maze.py`.

## Features

* Supports maze definitions stored in text files (see `maze-zero.txt`, `maze-one.txt`, etc)
* Implements a solver that works for 2-D matrix-based mazes
* Includes unit test(s) (`test_matrix2Dim.py`) and helper script (`matrix2Dim.py`)
* Written in Python for easy use and extension

## Requirements

* Python 3.11 or newer. ([GitHub][1])
* No other external dependencies explicitly listed (at least in the README).

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/AnastasiiaKulcsar/maze.git  
   cd maze  
   ```
2. Run the solver with a maze file, for example:

   ```bash
   python maze.py maze-one.txt  
   ```

   This will read the maze from `maze-one.txt` and output the solution (or path) in the console (or however the script is set up).

## Usage Example

```bash
python maze.py maze-one.txt  
```

You can also test with the other provided maze files (`maze-zero.txt`, `maze-many.txt`, `maze-cycle.txt`, etc).
(Adjust according to what `maze.py` supports.)

## Repository Structure

* `maze.py` — main solver script
* `matrix2Dim.py` — helper script / module for converting or dealing with 2D matrix representation
* `test_matrix2Dim.py` — unit tests for the matrix conversion or related logic
* `*.txt` — sample maze files: `maze-zero.txt`, `maze-one.txt`, `maze-many.txt`, `maze-cycle.txt`
* `README.md` — this file

## Technologies Used

* **Python 3.11+** — the primary programming language used in the project.
* **Standard Python modules** — The project appears to rely on built-in modules (no external library dependencies are specified).
* **Text-file input format** — Maze definitions are stored in plain text files, interpreted by `maze.py`.
* **Unit testing** — A basic unit test file (`test_matrix2Dim.py`) is included, so the `unittest` or similar built-in testing framework is likely used.

## Potential Improvements

* Add more documentation on the maze file format (how walls, paths, start/end are represented)
* Provide examples of solved output or visualization of the solution path
* Add error-handling for invalid maze files, no solution cases
* Extend the solver to support more algorithms (e.g., BFS, DFS, A*, etc)
* Add a requirements file or environments if external libraries are introduced
* Add CI (continuous integration) for automatic testing
* Add visualization / GUI to show the solved maze

[1]: https://github.com/AnastasiiaKulcsar/maze "GitHub - AnastasiiaKulcsar/maze: School Project"
