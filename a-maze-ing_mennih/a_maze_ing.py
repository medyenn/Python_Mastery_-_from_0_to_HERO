import sys
from maze_config import parse_config
from maze_generator.generator import MazeGenerator
from maze_solver import solve
from maze_writer import write_maze
from maze_display import run_display


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 a_maze_ing.py config.txt")
        sys.exit(1)

    config = parse_config(sys.argv[1])
    generator = MazeGenerator(config)
    grid = generator.generate()
    path_cells, path_str = solve(grid, config.entry, config.exit)
    write_maze(grid, path_str, config)
    run_display(grid, config, path_cells)


if __name__ == '__main__':
    main()
