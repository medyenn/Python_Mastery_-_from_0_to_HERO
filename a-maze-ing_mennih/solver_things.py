# from collections import deque
# from typing import Tuple, List


# def solve(
#     grid: List[List[int]],
#     entry: Tuple[int, int],
#     exit: Tuple[int, int]
# ) -> Tuple[List[Tuple[int, int]], str]:

#     queue = deque([(entry, [entry])])
#     visited = {entry}

#     while queue:
#         (r, c), path = queue.popleft()
#         if (r, c) == exit:
#             return path, build_direction_string(path)

#         # Check all 4 neighbors
#         for direction, (dr, dc), wall_bit, reverse_bit in [
#             ('N', (-1, 0), NORTH, SOUTH),
#             ('E', (0, +1), EAST,  WEST),
#             ('S', (+1, 0), SOUTH, NORTH),
#             ('W', (0, -1), WEST,  EAST),
#         ]:
#             nr, nc = r + dr, c + dc
#             if 0 <= nr < height and 0 <= nc < width:
#                 if not (grid[r][c] & wall_bit):  # wall is OPEN
#                     if (nr, nc) not in visited:
#                         visited.add((nr, nc))
#                         queue.append(((nr, nc), path + [(nr, nc)]))
