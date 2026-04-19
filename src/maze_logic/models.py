"""Core data models for maze generation and solving.

This module defines the fundamental structures for representing a maze:
- Direction: Cardinal directions (N, E, S, W)
- Cell: Individual maze cell with walls
- Maze: Complete maze grid with helper methods
- Path: Solution path representation
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import TypedDict


class Direction(Enum):
    """Cardinal directions with their bit positions for wall encoding.
    Bit positions match the output file format:
    NORTH = bit 0, EAST = bit 1, SOUTH = bit 2, WEST = bit 3
    """
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    @property
    def opposite(self) -> "Direction":
        """Return the opposite direction."""
        opposites = {
            Direction.NORTH: Direction.SOUTH,
            Direction.SOUTH: Direction.NORTH,
            Direction.EAST: Direction.WEST,
            Direction.WEST: Direction.EAST,
        }
        return opposites[self]

    def to_char(self) -> str:
        """Convert direction to movement character for path encoding."""
        chars = {
            Direction.NORTH: "N",
            Direction.SOUTH: "S",
            Direction.EAST: "E",
            Direction.WEST: "W",
        }
        return chars[self]

    @staticmethod
    def from_char(char: str) -> "Direction":
        """Convert movement character to direction."""
        char_map = {
            "N": Direction.NORTH,
            "S": Direction.SOUTH,
            "E": Direction.EAST,
            "W": Direction.WEST
        }
        if char not in char_map:
            raise ValueError(f"Invalid direction character: {char}")
        return char_map[char]

    def get_offset(self) -> tuple[int, int]:
        """Get (dx, dy) offset for this direction."""
        offsets = {
            Direction.NORTH: (0, -1),
            Direction.EAST: (1, 0),
            Direction.SOUTH: (0, 1),
            Direction.WEST: (-1, 0),
        }
        return offsets[self]


@dataclass
class Cell:
    """A single cell in the maze grid.

    Attributes:
        x: Column coordinate (0 to width-1)
        y: Row coordinate (0 to height-1)
        walls: Dictionary mapping Direction to bool. True = wall exists.
        is_visited: Tracks if visited during generation (for backtracking)
    """

    x: int
    y: int
    walls: dict[Direction, bool] = field(
        default_factory=lambda: {
            Direction.NORTH: True,
            Direction.EAST: True,
            Direction.SOUTH: True,
            Direction.WEST: True,
        }
    )
    is_visited: bool = False

    def __hash__(self) -> int:
        """Make Cell hashable by position."""
        return hash((self.x, self.y))

    def __eq__(self, other: object) -> bool:
        """Compare cells by position."""
        if not isinstance(other, Cell):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def has_wall(self, direction: Direction) -> bool:
        """Check if there is a wall in the given direction."""
        return self.walls[direction]

    def remove_wall(self, direction: Direction) -> None:
        """Remove wall in the given direction."""
        self.walls[direction] = False

    def add_wall(self, direction: Direction) -> None:
        """Add wall in the given direction."""
        self.walls[direction] = True

    def to_hex(self) -> str:
        """Convert cell walls to hexadecimal digit.

        Bits are set for walls that exist:
        - bit 0 (1): North wall
        - bit 1 (2): East wall
        - bit 2 (4): South wall
        - bit 3 (8): West wall

        Returns:
            Single hex digit (0-F) representing wall configuration
        """
        value = 0
        if self.walls[Direction.NORTH]:
            value |= 1 << Direction.NORTH.value
        if self.walls[Direction.EAST]:
            value |= 1 << Direction.EAST.value
        if self.walls[Direction.SOUTH]:
            value |= 1 << Direction.SOUTH.value
        if self.walls[Direction.WEST]:
            value |= 1 << Direction.WEST.value
        return f"{value:x}"


class Path(TypedDict):
    """Solution path from entry to exit.

    Attributes:
        entry: Starting coordinates (x, y)
        exit: Ending coordinates (x, y)
        steps: Path as string of N/E/S/W movements
    """

    entry: tuple[int, int]
    exit: tuple[int, int]
    steps: str


class Maze:
    """Complete maze grid with helper methods.

    Attributes:
        width: Number of columns
        height: Number of rows
        cells: 2D grid of Cell objects indexed by (x, y)
        entry: Starting position (x, y)
        exit: Ending position (x, y)
        solution_path: Shortest path from entry to exit (None if not solved)
    """

    def __init__(
        self,
        width: int,
        height: int,
        entry: tuple[int, int],
        exit: tuple[int, int],
    ) -> None:
        """Initialize an empty maze with all walls present.

        Args:
            width: Number of columns
            height: Number of rows
            entry: Starting position (x, y)
            exit: Ending position (x, y)

        Raises:
            ValueError: If dimensions are invalid or entry/exit out of bounds
        """
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")
        if not (0 <= entry[0] < width and 0 <= entry[1] < height):
            raise ValueError(f"Entry {entry} out of bounds ({width}x{height})")
        if not (0 <= exit[0] < width and 0 <= exit[1] < height):
            raise ValueError(f"Exit {exit} out of bounds ({width}x{height})")
        if entry == exit:
            raise ValueError("Entry and exit must be different")

        self.width: int = width
        self.height: int = height
        self.entry: tuple[int, int] = entry
        self.exit: tuple[int, int] = exit
        self.solution_path: Path | None = None

        # Initialize cell grid
        self.cells: dict[tuple[int, int], Cell] = {}
        for y in range(height):
            for x in range(width):
                self.cells[(x, y)] = Cell(x, y)

    def get_cell(self, x: int, y: int) -> Cell:
        """Get cell at coordinates.

        Args:
            x: Column coordinate
            y: Row coordinate

        Returns:
            Cell at (x, y)

        Raises:
            IndexError: If coordinates are out of bounds
        """
        if not (0 <= x < self.width and 0 <= y < self.height):
            raise IndexError(f"Coordinates ({x}, {y}) out of bounds",
                             f"({self.width}x{self.height})")
        return self.cells[(x, y)]

    def get_neighbors(self, x: int, y: int) -> list[tuple[Direction, Cell]]:
        """Get valid neighboring cells and the direction to reach them.

        Args:
            x: Column coordinate
            y: Row coordinate

        Returns:
            List of (Direction, Cell) tuples for valid neighbors

        Raises:
            IndexError: If coordinates are out of bounds
        """
        self.get_cell(x, y)
        neighbors: list[tuple[Direction, Cell]] = []

        for direction in Direction:
            dx, dy = direction.get_offset()
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height:
                neighbor = self.get_cell(nx, ny)
                neighbors.append((direction, neighbor))

        return neighbors

    def has_passage(self, x1: int, y1: int, x2: int, y2: int) -> bool:
        """Check if there is a passage (no wall) between two adjacent cells.

        A passage exists if both cells have removed their shared wall.

        Args:
            x1, y1: First cell coordinates
            x2, y2: Second cell coordinates

        Returns:
            True if passage exists, False otherwise

        Raises:
            ValueError: If cells are not adjacent
        """
        cell1 = self.get_cell(x1, y1)
        cell2 = self.get_cell(x2, y2)

        dx = x2 - x1
        dy = y2 - y1

        if abs(dx) + abs(dy) != 1:
            raise ValueError(
                f"Cells ({x1}, {y1}) and ({x2}, {y2}) are not adjacent")

        # Determine direction from cell1 to cell2
        if dx == 1:
            direction = Direction.EAST
        elif dx == -1:
            direction = Direction.WEST
        elif dy == 1:
            direction = Direction.SOUTH
        else:  # dy == -1
            direction = Direction.NORTH

        # Check if both cells have no wall in the shared direction
        return (not cell1.has_wall(direction) and
                not cell2.has_wall(direction.opposite))

    def remove_wall_between(self, x1: int, y1: int, x2: int, y2: int) -> None:
        """Remove wall between two adjacent cells (create passage).

        Updates both cells to maintain wall coherence.

        Args:
            x1, y1: First cell coordinates
            x2, y2: Second cell coordinates

        Raises:
            ValueError: If cells are not adjacent
        """
        cell1 = self.get_cell(x1, y1)
        cell2 = self.get_cell(x2, y2)

        dx = x2 - x1
        dy = y2 - y1

        if abs(dx) + abs(dy) != 1:
            raise ValueError(
                f"Cells ({x1}, {y1}) and ({x2}, {y2}) are not adjacent")

        # Determine direction from cell1 to cell2
        if dx == 1:
            direction = Direction.EAST
        elif dx == -1:
            direction = Direction.WEST
        elif dy == 1:
            direction = Direction.SOUTH
        else:  # dy == -1
            direction = Direction.NORTH

        # Remove walls in both cells
        cell1.remove_wall(direction)
        cell2.remove_wall(direction.opposite)

    def is_fully_connected(self) -> bool:
        """Check if all cells are reachable from entry.

        Uses BFS to explore from entry. If all cells are visited,
        the maze is fully connected.

        Returns:
            True if maze is fully connected, False otherwise
        """
        from collections import deque

        visited: set[tuple[int, int]] = set()
        queue: deque[tuple[int, int]] = deque([self.entry])
        visited.add(self.entry)

        while queue:
            x, y = queue.popleft()
            for direction, neighbor in self.get_neighbors(x, y):
                if self.has_passage(x, y, neighbor.x, neighbor.y):
                    key = (neighbor.x, neighbor.y)
                    if key not in visited:
                        visited.add(key)
                        queue.append(key)

        return len(visited) == self.width * self.height
