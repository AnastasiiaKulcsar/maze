import sys
from matrix2Dim import Matrix2Dim

# Maze character to internal representation
CHAR_TO_CODE = {'*': 0, ' ': 1, 'A': 2, 'B': 3}
CODE_TO_CHAR = {0: '*', 1: ' ', 2: 'A', 3: 'B'}

# Directions with vector deltas
DIRS = {
    'N': (-1, 0),
    'S': (1, 0),
    'E': (0, 1),
    'W': (0, -1)
}

class Maze:
    def __init__(self, filename: str):
        self.grid, self.path_grid, self.start, self.end = self.read_maze(filename)

    def read_maze(self, filename: str):
        with open(filename, 'r') as f:
            lines = [line.rstrip('\n') for line in f if line.strip()]

        rows = len(lines)
        cols = len(lines[0])
        matrix_data = []
        path_data = []

        start = end = None

        for r, line in enumerate(lines):
            row = []
            path_row = list(line)
            for c, char in enumerate(line):
                val = CHAR_TO_CODE.get(char, 0)
                row.append(val)
                if char == 'A':
                    start = (r, c)
                elif char == 'B':
                    end = (r, c)
            matrix_data.append(row)
            path_data.append(path_row)

        if start is None or end is None:
            raise ValueError("Maze must have 'A' and 'B' defined.")

        return Matrix2Dim((rows, cols), matrix_data), path_data, start, end

    def in_bounds(self, r, c):
        rows, cols = self.grid._dimensions
        return 0 <= r < rows and 0 <= c < cols

    def find_path(self):
        visited = set()
        path = []

        def dfs(r, c):
            if (r, c) in visited:
                return False
            visited.add((r, c))

            if (r, c) == self.end:
                return True

            for dir_name, (dr, dc) in DIRS.items():
                nr, nc = r + dr, c + dc
                if self.in_bounds(nr, nc):
                    val = self.grid.get_element(nr, nc)
                    if val in (1, 3) and (nr, nc) not in visited:
                        if dfs(nr, nc):
                            path.append(((nr, nc), dir_name))
                            return True
            return False

        found = dfs(*self.start)
        return path[::-1] if found else None

    def apply_path(self, path):
        for (r, c), dir_char in path:
            if self.path_grid[r][c] not in ('A', 'B'):
                self.path_grid[r][c] = dir_char

    def print_path_maze(self):
        rows = len(self.path_grid)
        cols = len(self.path_grid[0])

        print(" " * ((cols // 2) - 1) + "N\n")  # Top label

        for i, row in enumerate(self.path_grid):
            if i == rows // 2:
                print("w ", end="")  # Left side label (middle row)
            else:
                print("  ", end="")
            print(''.join(row), end="")
            if i == rows // 2:
                print("   E")  # Right side label
            else:
                print()

        print("\n" + " " * ((cols // 2) - 1) + "S")  # Bottom label


def main():
    if len(sys.argv) != 2:
        print("Usage: python maze.py <maze_file>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        maze = Maze(filename)
        path = maze.find_path()

        if path:
            maze.apply_path(path)
            maze.print_path_maze()
            path_str = ''.join(dir_char for (_, dir_char) in path)
            print(f"\nFor this example, the path from 'A' to 'B' is \"{path_str}\".")
            print(f"The length of the path is {len(path)}.")
        else:
            print("No path found from A to B.")

    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    main()
