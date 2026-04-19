import time
from collections import deque
from typing import (
    List, Tuple, Dict, Set, Deque, Optional)
from maze_displayer import (
    draw_cell, DEFAULT_COLORS, NORTH, EAST, SOUTH, WEST)


DIRECTIONS: List[Tuple[int, int, int, str]] = [
    (NORTH, -1,  0, 'N'),
    (EAST,   0, +1, 'E'),
    (SOUTH, +1,  0, 'S'),
    (WEST,   0, -1, 'W'),
]


def _bfs(
    grid: List[List[int]],
    height: int,
    width: int,
    entry: Tuple[int, int],
    exit_: Tuple[int, int],
) -> Optional[Dict[Tuple[int, int], Tuple[int, int]]]:
    """
    Run BFS from entry to exit and return the came_from dictionary.

    came_from maps every visited cell to the cell it was reached from.
    Use this to reconstruct the path by backtracking from exit_ to entry.

    Returns None if no path exists (should not happen in a valid maze).

    Args:
        grid:   2D list — grid[row][col] = int 0-15
        height: number of maze rows
        width:  number of maze columns
        entry:  (row, col) start cell
        exit_:  (row, col) target cell

    Returns:
        came_from dict if path found, None otherwise
    """
    queue: Deque[Tuple[int, int]] = deque()
    queue.append(entry)

    visited: Set[Tuple[int, int]] = set()
    visited.add(entry)

    came_from: Dict[Tuple[int, int], Tuple[int, int]] = {}

    while queue:
        current: Tuple[int, int] = queue.popleft()
        r, c = current

        if current == exit_:
            return came_from

        for wall_bit, dr, dc, _ in DIRECTIONS:
            if grid[r][c] & wall_bit:
                continue

            nr: int = r + dr
            nc: int = c + dc

            if not (0 <= nr < height and 0 <= nc < width):
                continue

            if (nr, nc) in visited:
                continue

            visited.add((nr, nc))
            came_from[(nr, nc)] = current
            queue.append((nr, nc))

    return None


def _reconstruct_path(
    came_from: Dict[Tuple[int, int], Tuple[int, int]],
    entry: Tuple[int, int],
    exit_: Tuple[int, int],
) -> Tuple[List[Tuple[int, int]], str]:
    """
    Backtrack through came_from to build the path from entry to exit.

    Also derives the direction string (e.g. 'SSWWNE') by comparing
    each consecutive pair of cells in the path.

    Args:
        came_from: dict from _bfs mapping each cell to its predecessor
        entry:     (row, col) start cell
        exit_:     (row, col) end cell

    Returns:
        path_coords: list of (row, col) tuples from entry to exit
        path_str:    direction string e.g. 'SSWWNEEE'
    """
    path: List[Tuple[int, int]] = []
    current: Tuple[int, int] = exit_

    while current != entry:
        path.append(current)
        current = came_from[current]
    path.append(entry)

    path.reverse()

    direction_chars: List[str] = []
    for i in range(len(path) - 1):
        r0, c0 = path[i]
        r1, c1 = path[i + 1]
        dr: int = r1 - r0
        dc: int = c1 - c0

        if dr == -1:
            direction_chars.append('N')
        elif dr == +1:
            direction_chars.append('S')
        elif dc == +1:
            direction_chars.append('E')
        elif dc == -1:
            direction_chars.append('W')

    return path, ''.join(direction_chars)


def solve_silent(
    grid: List[List[int]],
    height: int,
    width: int,
    entry: Tuple[int, int],
    exit_: Tuple[int, int],
) -> Tuple[List[Tuple[int, int]], str]:
    """
    Find the shortest path using BFS with no display or animation.

    Use this when you only need the path for the output file,
    not for visual display.

    Args:
        grid:   2D list — grid[row][col] = int 0-15
        height: number of maze rows
        width:  number of maze columns
        entry:  (row, col) start cell
        exit_:  (row, col) target cell

    Returns:
        path_coords: list of (row, col) from entry to exit
        path_str:    direction string e.g. 'SSWWNEEE'

    Raises:
        ValueError if no path exists
    """
    came_from: Optional[Dict[Tuple[int, int], Tuple[int, int]]] = _bfs(
        grid, height, width, entry, exit_
    )

    if came_from is None:
        raise ValueError(
            f"No path found from {entry} to {exit_} — maze may be invalid"
        )

    return _reconstruct_path(came_from, entry, exit_)


def solve_animated(
    grid: List[List[int]],
    height: int,
    width: int,
    entry: Tuple[int, int],
    exit_: Tuple[int, int],
    cell_states: Dict[Tuple[int, int], str],
    colors: Dict[str, str],
    speed: float = 0.03,
) -> Tuple[List[Tuple[int, int]], str]:
    """
    Find the shortest path using BFS with live terminal animation.

    Phase 1 — Exploration:
        Each cell BFS dequeues is painted 'visited' (yellow).
        This shows the wavefront spreading from entry outward.

    Phase 2 — Backtracking:
        Once the exit is found, cells on the shortest path are painted
        'path' (green) one by one from exit back to entry.
        All other visited cells remain yellow.

    After this function returns, cell_states reflects the final visual
    state of every cell. The menu can repaint colors without re-running BFS.

    Args:
        grid:        2D list — grid[row][col] = int 0-15
        height:      number of maze rows
        width:       number of maze columns
        entry:       (row, col) start cell
        exit_:       (row, col) target cell
        cell_states: dict to update — maps (row, col) to state string
        colors:      ANSI color dict passed to draw_cell
        speed:       seconds to sleep between each cell paint

    Returns:
        path_coords: list of (row, col) from entry to exit
        path_str:    direction string e.g. 'SSWWNEEE'

    Raises:
        ValueError if no path exists
    """
    queue: Deque[Tuple[int, int]] = deque()
    queue.append(entry)

    visited: Set[Tuple[int, int]] = set()
    visited.add(entry)

    came_from: Dict[Tuple[int, int], Tuple[int, int]] = {}
    found: bool = False

    while queue:
        current: Tuple[int, int] = queue.popleft()
        r, c = current

        if current != entry and current != exit_:
            cell_states[current] = "visited"
            draw_cell(r, c, "visited", colors, height, width, enforce_borders(grid))
            time.sleep(speed)

        if current == exit_:
            found = True
            break

        for wall_bit, dr, dc, _ in DIRECTIONS:
            if grid[r][c] & wall_bit:
                continue
            nr, nc = r + dr, c + dc
            if not (0 <= nr < height and 0 <= nc < width):
                continue
            if (nr, nc) in visited:
                continue
            visited.add((nr, nc))
            came_from[(nr, nc)] = current
            queue.append((nr, nc))

    if not found:
        raise ValueError(
            f"No path found from {entry} to {exit_} — maze may be invalid"
        )

    path, path_str = _reconstruct_path(came_from, entry, exit_)

    for cell in path:
        r, c = cell
        if cell != entry and cell != exit_:
            cell_states[cell] = "path"
            draw_cell(r, c, "path", colors, height, width, enforce_borders(grid))
            time.sleep(speed)

    return path, path_str


if __name__ == "__main__":
    import sys
    sys.path.insert(0, '/tmp')

    from maze_displayer import draw_maze_static, enforce_borders

    fake_grid = [
        [9, 3, 13, 1, 5, 5, 1, 3, 9, 5, 5, 3, 9, 1, 5, 5, 3, 9, 3, 13],
        [14, 12, 3, 12, 7, 9, 6, 10, 10, 9, 3, 12, 6, 10, 11, 9, 6, 1, 12, 10],
        [9, 3, 12, 3, 9, 6, 11, 10, 14, 10, 12, 5, 5, 6, 8, 6, 9, 4, 5, 5],
        [10, 12, 7, 10, 10, 13, 2, 10, 9, 6, 9, 5, 5, 3, 10, 13, 4, 3, 9, 6],
        [8, 5, 5, 6, 8, 3, 12, 4, 6, 9, 6, 9, 5, 6, 12, 5, 3, 10, 10, 0],
        [12, 5, 3, 13, 2, 3, 3, 13, 5, 4, 3, 12, 1, 5, 7, 9, 6, 10, 12, 7],
        [13, 3, 12, 3, 12, 7, 12, 3, 9, 5, 8, 11, 10, 9, 2, 6, 9, 4, 7, 12],
        [9, 4, 7, 12, 5, 9, 5, 6, 8, 3, 9, 4, 6, 10, 9, 7, 8, 7, 9, 6],
        [10, 9, 5, 5, 1, 5, 5, 3, 14, 10, 10, 9, 7, 10, 14, 9, 6, 9, 6, 12],
        [10, 12, 3, 11, 10, 9, 3, 12, 5, 6, 12, 2, 9, 6, 10, 12, 3, 10, 13, 8],
        [10, 9, 4, 6, 10, 10, 12, 5, 5, 5, 3, 10, 12, 3, 12, 5, 2, 10, 9, 5],
        [10, 10, 11, 9, 6, 12, 1, 9, 5, 3, 12, 4, 7, 12, 5, 3, 10, 10, 10, 12],
        [10, 12, 2, 10, 13, 5, 6, 12, 3, 12, 5, 5, 1, 7, 9, 6, 10, 12, 6, 12],
        [10, 9, 6, 10, 9, 3, 9, 3, 7, 3, 13, 3, 12, 3, 10, 13, 4, 5, 7, 12],
        [12, 4, 7, 12, 6, 12, 6, 12, 5, 4, 5, 4, 7, 12, 4, 5, 5, 5, 5, 8],
    ]

    enforce_borders(fake_grid)
    H: int = len(fake_grid)
    W: int = len(fake_grid[0])
    entry:  Tuple[int, int] = (0, 0)
    exit_:  Tuple[int, int] = (H - 1, W - 1)
    cell_states: Dict[Tuple[int, int], str] = {}

    path_coords, path_str = solve_silent(fake_grid, H, W, entry, exit_)
    print(
        f"Silent solve: {len(path_coords)} cells, "
        "path starts {path_coords[:4]}")
    print(f"Direction string (first 20): {path_str[:20]}...")
    print(f"Path ends at: {path_coords[-1]}  (should be {exit_})")
    print()

    input("Press Enter to run the animated BFS...")
    draw_maze_static(
        fake_grid, H, W, entry, exit_, cell_states, DEFAULT_COLORS)
    solve_animated(
        fake_grid, H, W, entry, exit_,
        cell_states, DEFAULT_COLORS,
        speed=0.02
    )

    import sys
    sys.stdout.write(f"\033[{H * 2 + 4};1H")
    sys.stdout.flush()
    print(f"\nAnimation complete. Path length: {len(path_coords)} cells")
    print(f"Direction string (first 30): {path_str[:30]}...")


# class Path_finder:

#     DIRECTIONS: list[tuple] = [
#         (0, -1, 1, 4),
#         (1, 0, 2, 8),
#         (0, 1, 4, 1),
#         (-1, 0, 8, 2)
#     ]

#     def __init__(
#         self,
#         WIDTH: int,
#         HEIGHT: int,
#         ENTRY: Tuple[int, int],
#         EXIT: Tuple[int, int],
#         OUTPUT_FILE: str,
#         PERFECT: Optional[bool],
#         SEED: Optional[int] = None
#     ) -> None:

#         self.WIDTH: int = WIDTH
#         self.HEIGHT: int = HEIGHT
#         self.ENTRY: Tuple[int, int] = ENTRY
#         self.EXIT: Tuple[int, int] = EXIT
#         self.OUTPUT_FILE: str = OUTPUT_FILE
#         self.PERFECT: Optional[bool] = PERFECT
#         self.SEED: Optional[int] = SEED
#         self.grid: List[List[Cell]] = [
#                 [
#                     Cell(15) for _ in range(self.WIDTH)
#                 ] for _ in range(self.HEIGHT)
#             ]
#         self.solution_path: List[tuple] = []
#         self.show_path: bool = False
#         self.render_animation: bool = False
#         self.animation_speed: float = 0.005
#         self.wall_color: Dict[str, str] = {
#             "name": "Green",
#             "value": "\033[38;2;86;130;3m"
#         }
#         self.solution_color: Dict[str, str] = {
#             "name": "Yellow",
#             "value": "\033[38;2;255;213;0m"
#         }
#         self.pattern_color: Dict[str, str] = {
#             "name": "Green",
#             "value": "\033[38;2;86;130;3m"
#         }

#     def find_solution(self) -> None:

#         directions: List[tuple] = [
#             (0, -1, 1),   # North
#             (1,  0, 2),   # East
#             (0,  1, 4),   # South
#             (-1, 0, 8),   # West
#         ]

#         came_from: Dict = {self.ENTRY: None}
#         queue: deque = deque([self.ENTRY])

#         while queue:
#             current_x, current_y = queue.popleft()

#             if (current_x, current_y) == self.EXIT:
#                 break

#             current_walls: int = self.grid[current_y][current_x].walls

#             for dx, dy, wall_mask in directions:
#                 nx: int = current_x + dx
#                 ny: int = current_y + dy

#                 if (
#                     (0 <= nx < self.WIDTH)
#                     and (0 <= ny < self.HEIGHT)
#                     and (current_walls & wall_mask) == 0
#                     and (nx, ny) not in came_from
#                 ):
#                     came_from[(nx, ny)] = (current_x, current_y)
#                     queue.append((nx, ny))

#         self.solution_path = []
#         cell: Optional[Tuple[int, int]] = self.EXIT

#         while cell is not None:
#             self.solution_path.append(cell)
#             cell = came_from.get(cell)

#         self.solution_path.reverse()
