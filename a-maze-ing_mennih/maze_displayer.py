# import os
import sys
from typing import List, Dict, Tuple
import shutil


NORTH, EAST, SOUTH, WEST = 1, 2, 4, 8


fa_grid = [
    [9, 3, 13, 1, 5, 5, 1, 3, 9, 5, 5, 3, 9, 1, 5, 5, 3, 9, 3, 13],
    [14, 12, 3, 12, 7, 9, 6, 10, 10, 9, 3, 12, 6, 10, 11, 9, 6, 10, 12, 10],
    [9, 3, 12, 3, 9, 6, 11, 10, 14, 10, 12, 5, 5, 6, 8, 6, 9, 4, 5, 5],
    [10, 12, 7, 10, 10, 13, 2, 10, 9, 6, 9, 5, 5, 3, 10, 13, 4, 3, 9, 6],
    [8, 5, 5, 6, 8, 3, 12, 4, 6, 9, 6, 9, 5, 6, 12, 5, 3, 10, 10, 0],
    [12, 5, 3, 13, 2, 3, 3, 13, 5, 4, 3, 12, 1, 5, 7, 9, 6, 10, 12, 7],
    [13, 3, 12, 3, 12, 7, 12, 3, 9, 5, 8, 11, 10, 9, 2, 6, 9, 4, 7, 12],
    [9, 4, 7, 12, 5, 5, 5, 6, 8, 3, 9, 4, 6, 10, 9, 7, 8, 7, 9, 6],
    [10, 9, 5, 5, 1, 5, 5, 3, 14, 10, 10, 9, 7, 10, 14, 9, 6, 9, 6, 12],
    [10, 12, 3, 11, 10, 9, 3, 12, 5, 6, 12, 2, 9, 6, 10, 12, 3, 10, 13, 8],
    [10, 9, 4, 6, 10, 10, 12, 5, 5, 5, 3, 10, 12, 3, 12, 5, 2, 10, 9, 5],
    [10, 10, 11, 9, 6, 12, 10, 9, 5, 3, 12, 4, 7, 12, 5, 3, 10, 10, 10, 12],
    [10, 12, 2, 10, 13, 5, 6, 12, 3, 12, 5, 5, 1, 7, 9, 6, 10, 12, 6, 12],
    [10, 9, 6, 10, 9, 3, 9, 3, 7, 3, 13, 3, 12, 3, 10, 13, 4, 5, 7, 12],
    [12, 4, 7, 12, 6, 12, 6, 12, 5, 4, 5, 4, 7, 12, 4, 5, 5, 5, 5, 8]
]


RESET = "\033[0m"
WALL_CHAR = '██'
EMPTY_CHAR = '  '


def color(code: int) -> str:
    return f"\033[38;5;{code}m"


DEFAULT_COLORS: Dict[str, str] = {
    "wall":    color(28),
    "floor":   RESET,
    "entry":   color(226),
    "exit":    color(196),
    "path":    color(21),
    "visited": color(39),
    "pattern": color(27),
}


def enforce_borders(grid: List[List[int]]) -> List[List[int]]:

    H: int = len(grid)
    W: int = len(grid[0])

    for c in range(W):
        grid[0][c] |= NORTH
        grid[H - 1][c] |= SOUTH

    for r in range(H):
        grid[r][0] |= WEST
        grid[r][W - 1] |= EAST

    return grid


fake_grid = enforce_borders(fa_grid)


def cell_to_terminal(row, col):
    """computes the terminal coordinates of a cell's interior"""
    terminal_row: int = row * 2 + 2
    terminal_col: int = col * 4 + 3
    return (terminal_row, terminal_col)


def build_buffer(f_grid, height, width, entry, f_exit, cell_states, colors):
    """builds the 2D character buffer"""

    buf_h = height*2 + 1
    buf_w = width*2 + 1

    wall_char: str = colors["wall"] + WALL_CHAR + RESET
    buf: List[List[str]] = [
        [wall_char] * buf_w for _ in range(buf_h)
    ]

    for r in range(height):
        for c in range(width):
            cell_val = f_grid[r][c]
            if not (cell_val & NORTH):
                buf[r * 2][c * 2 + 1] = EMPTY_CHAR
            if not (cell_val & WEST):
                buf[r * 2 + 1][c * 2] = EMPTY_CHAR
            if (r, c) == entry:
                interior: str = colors["entry"] + RESET
            elif (r, c) == f_exit:
                interior = colors["exit"] + RESET
            else:
                state: str = cell_states.get((r, c), "floor")
                interior = colors.get(state, RESET) + EMPTY_CHAR + RESET

                buf[r * 2 + 1][c * 2 + 1] = interior

    for r in range(height):
        if not (f_grid[r][width - 1] & EAST):
            buf[r * 2 + 1][buf_w - 1] = EMPTY_CHAR
    for c in range(width):
        if not (f_grid[height - 1][c] & SOUTH):
            buf[buf_h - 1][c * 2 + 1] = EMPTY_CHAR

    return buf


def print_buffer(buf):
    output: str = "\n".join("".join(row) for row in buf) + "\n"
    sys.stdout.write(output)
    sys.stdout.flush()


def clear_screen():
    """rints \033[2J\033[H"""
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()


def draw_maze_static(
    grid: List[List[int]],
    height: int,
    width: int,
    entry: Tuple[int, int],
    exit_: Tuple[int, int],
    cell_states: Dict[Tuple[int, int], str],
    colors: Dict[str, str],
) -> None:
    """prints the buffer to terminal"""
    clear_screen()
    buf: List[List[str]] = build_buffer(
        grid, height, width, entry, exit, cell_states, colors
    )
    print_buffer(buf)


TERMINAL_rows, _ = shutil.get_terminal_size()


def draw_cell(row, col, state, colors, height, width, grid):
    """moves cursor to (term_row, term_col)
    prints the correctly colored character
    moves cursor back to a safe position (bottom of screen)."""
    if not (0 <= row < height and 0 <= col < width):
        return

    terminal_row, terminal_col = cell_to_terminal(row, col)

    sys.stdout.write(f'\033[{terminal_row};{terminal_col}H')
    sys.stdout.write(colors.get(state))
    sys.stdout.write(WALL_CHAR)

    if state in ['visited', 'path']:
        cell_val: int = grid[row][col]
        if not (cell_val & NORTH):
            sys.stdout.write(f'\033[{terminal_row - 1};{terminal_col}H')
            sys.stdout.write(colors.get(state))
            sys.stdout.write(WALL_CHAR)
        elif not (cell_val & SOUTH):
            sys.stdout.write(f'\033[{terminal_row - 1};{terminal_col}H')
            sys.stdout.write(colors.get(state))
            sys.stdout.write(WALL_CHAR)
        if not (cell_val & WEST):
            sys.stdout.write(f'\033[{terminal_row};{terminal_col - 2}H')
            sys.stdout.write(colors.get(state))
            sys.stdout.write(WALL_CHAR)
        elif not (cell_val & EAST):
            sys.stdout.write(f'\033[{terminal_row};{terminal_col + 2}H')
            sys.stdout.write(colors.get(state))
            sys.stdout.write(WALL_CHAR)

    color_str = colors.get(state, RESET)
    sys.stdout.write(color_str + RESET)

    sys.stdout.write(f"\033[{TERMINAL_rows};1H")

    sys.stdout.flush()


# def draw_cell(
#     row: int,
#     col: int,
#     state: str,
#     colors: Dict[str, str],
#     height: int,
#     width: int,
#     grid: List[List[int]],
# ) -> None:
#     """
#     Repaint one cell's interior AND its open wall slots.

#     Paints the cell interior plus any adjacent wall slots where
#     the wall is open. This prevents the checkerboard gap effect
#     that appears when only the interior is colored.

#     Args:
#         row:    maze row (0-indexed)
#         col:    maze column (0-indexed)
#         state:  color state key e.g. 'visited', 'path', 'floor'
#         colors: dict mapping state name to ANSI color string
#         height: number of maze rows
#         width:  number of maze columns
#         grid:   the maze grid — needed to check wall bits
#     """
#     if not (0 <= row < height and 0 <= col < width):
#         return

#     term_row: int
#     term_col: int
#     term_row, term_col = cell_to_terminal(row, col)

#     color_str: str = colors.get(state, RESET)

#     sys.stdout.write(f'\033[{term_row};{term_col}H')
#     sys.stdout.write(colors.get(state))
#     sys.stdout.write(WALL_CHAR)

#     color_str = colors.get(state, RESET)
#     sys.stdout.write(color_str + RESET)


# def draw_cell_walls(
#     row: int,
#     col: int,
#     state: str,
#     colors: Dict[str, str],
#     height: int,
#     width: int,
#     grid: List[List[int]]
# ):
#     term_row: int
#     term_col: int
#     term_row, term_col = cell_to_terminal(row, col)

#     cell_val: int = grid[row][col]

#     if not (cell_val & NORTH):
#         draw_cell(row - 1, col, state, colors, height, width,)

#     if not (cell_val & SOUTH):
#         draw_cell(row + 1, col, state, colors, height, width,)

#     if not (cell_val & WEST):
#         draw_cell(row, col - 2, state, colors, height, width,)

#     if not (cell_val & EAST):
#         draw_cell(row, col + 2, state, colors, height, width,)


def main():
    # import time

    enforce_borders(fake_grid)

    H: int = len(fake_grid)
    W: int = len(fake_grid[0])

    entry:  Tuple[int, int] = (0, 0)
    exit_:  Tuple[int, int] = (H - 1, W - 1)

    draw_maze_static(fake_grid, H, W, entry, exit_, {}, DEFAULT_COLORS)

    # test_cells = [
    #     (2,  3,  "visited"),
    #     (5,  10, "visited"),
    #     (8,  15, "path"),
    #     (11, 7,  "path")
    # ]

    draw_cell(0, 0, 'entry', DEFAULT_COLORS, H, W, fake_grid)
    draw_cell(14, 19, 'exit', DEFAULT_COLORS, H, W, fake_grid)

    # for r, c, s in test_cells:
    #     time.sleep(0.4)
    #     draw_cell(r, c, s, DEFAULT_COLORS, H, W, fake_grid)


main()
