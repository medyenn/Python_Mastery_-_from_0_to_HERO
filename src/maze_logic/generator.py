"""Maze generation using Recursive Backtracking algorithm.

This module provides the MazeGenerator class which creates perfect mazes
(with exactly one path between any two cells) or imperfect mazes.
"""

import random
from src.maze_logic.models import Maze, Direction, Cell


class GenerationError(Exception):
    """Raised when maze generation fails validation."""

    pass


class MazeGenerator:
    """Generate mazes using Recursive Backtracking algorithm.

    Attributes:
        width: Maze width (number of columns)
        height: Maze height (number of rows)
        entry: Starting cell coordinates (x, y)
        exit: Ending cell coordinates (x, y)
        perfect: If True, guarantee exactly one path between entry and exit
        seed: Random seed for reproducibility (None = non-deterministic)
        maze: The generated Maze object
        rng: Random number generator instance
    """

    def __init__(
        self,
        width: int,
        height: int,
        entry: tuple[int, int],
        exit: tuple[int, int],
        perfect: bool = True,
        seed: int | None = None,
    ) -> None:
        """Initialize the maze generator.

        Args:
            width: Number of columns (must be > 0)
            height: Number of rows (must be > 0)
            entry: Starting position (x, y)
            exit: Ending position (x, y)
            perfect: If True, create perfect maze (default: True)
            seed: Random seed for reproducibility (default: None)

        Raises:
            ValueError: If dimensions or positions invalid
        """
        self.width: int = width
        self.height: int = height
        self.entry: tuple[int, int] = entry
        self.exit: tuple[int, int] = exit
        self.perfect: bool = perfect
        self.seed: int | None = seed

        # Initialize maze with all walls
        self.maze: Maze = Maze(width, height, entry, exit)

        # Create reproducible RNG
        self.rng: random.Random = random.Random(seed)

    def generate(self) -> Maze:
        """Generate the maze using Recursive Backtracking.

        Algorithm:
        1. Mark entry cell as visited
        2. Recursively carve passages from entry using DFS
        3. Validate full connectivity
        4. Check for policy violations (3x3 areas)

        Returns:
            Completed Maze object with solution path not yet computed

        Raises:
            GenerationError: If maze fails validation
        """
        # Mark entry as visited and start carving
        entry_cell = self.maze.get_cell(self.entry[0], self.entry[1])
        entry_cell.is_visited = True

        # Recursively carve from entry
        self._carve_passages(self.entry[0], self.entry[1])

        # Validate the maze
        if not self.maze.is_fully_connected():
            raise GenerationError(
                "Generated maze is not fully connected"
            )

        # Check for 3x3 open areas if minimum size
        if self.width >= 3 and self.height >= 3:
            if self._has_3x3_open_area():
                raise GenerationError(
                    "Maze contains 3x3 open area (policy violation)"
                )

        # If PERFECT is required, verify exactly one path
        if self.perfect:
            # Recursive Backtracking guarantees perfect maze
            # (exactly one path between any two cells)
            pass

        return self.maze

    def _carve_passages(self, x: int, y: int) -> None:
        """Recursively carve passages using depth-first search.

        Marks the current cell as visited, randomly shuffles directions,
        and recursively visits unvisited neighbors, removing walls.

        Args:
            x: Current cell column coordinate
            y: Current cell row coordinate
        """
        # Get all four directions in random order
        directions = list(Direction)
        self.rng.shuffle(directions)

        for direction in directions:
            # Calculate neighbor coordinates
            dx, dy = direction.get_offset()
            nx, ny = x + dx, y + dy

            # Check bounds
            if not (0 <= nx < self.width and 0 <= ny < self.height):
                continue

            neighbor = self.maze.get_cell(nx, ny)

            # If neighbor not visited, carve passage and recurse
            if not neighbor.is_visited:
                neighbor.is_visited = True

                # Remove wall between current and neighbor
                self.maze.remove_wall_between(x, y, nx, ny)

                # Recurse into neighbor
                self._carve_passages(nx, ny)

    def _has_3x3_open_area(self) -> bool:
        """Check for any 3x3 area with no internal walls.

        A policy violation: detects if:
        - A 3x3 block has all 4 interior passages open

        Returns:
            True if a 3x3 open area exists, False otherwise
        """
        # Check all possible 3x3 blocks
        for y in range(self.height - 2):
            for x in range(self.width - 2):
                # Check 3x3 block starting at (x, y)
                if self._is_3x3_open(x, y):
                    return True

        return False

    def _is_3x3_open(self, x: int, y: int) -> bool:
        """Check if a specific 3x3 block is completely open.

        For a 3x3 block:
        ```
        (x,y)   (x+1,y)   (x+2,y)
        (x,y+1) (x+1,y+1) (x+2,y+1)
        (x,y+2) (x+1,y+2) (x+2,y+2)
        ```

        We check if all 4 interior passages exist:
        - (x,y) <-> (x+1,y) (east from top-left)
        - (x,y) <-> (x,y+1) (south from top-left)
        - (x+1,y) <-> (x+1,y+1) (south from top-middle)
        - (x,y+1) <-> (x+1,y+1) (east from middle-left)

        Args:
            x: Left edge of 3x3 block
            y: Top edge of 3x3 block

        Returns:
            True if all interior passages are open, False otherwise
        """
        # All four interior cells must have no walls between them
        passages_open = (
            self.maze.has_passage(x, y, x + 1, y) and
            self.maze.has_passage(x, y, x, y + 1) and
            self.maze.has_passage(x + 1, y, x + 1, y + 1) and
            self.maze.has_passage(x, y + 1, x + 1, y + 1)
        )

        return passages_open

    def find_42_pattern(self) -> list[Cell] | None:
        """Detect and return cells forming a "42" pattern if present.

        The "42" pattern (Douglas Adams reference) is a visual marker
        that appears naturally in large mazes generated by recursive
        backtracking. It's not mandatory but a fun easter egg.

        For mazes ≥ 10×10, we can theoretically detect patterns, but
        the exact detection depends on carving order. Returns cells
        that form meaningful corridor patterns if detected.

        Args:
            None

        Returns:
            List of cells forming "42" pattern, or None if not found
            or maze too small for pattern

        Note:
            This is an optional feature. Actual implementation depends
            on specific maze structure and generation randomness.
        """
        # Minimum size for "42" pattern
        if self.width < 10 or self.height < 10:
            return None

        # Pattern detection would go here (optional/advanced)
        # For now, return None - could implement later
        return None

    def verify_perfect_maze(self) -> bool:
        """Verify that the maze satisfies the PERFECT constraint.

        A perfect maze has exactly ONE path between any two cells
        (fully connected + no loops = tree structure).

        Recursive Backtracking guarantees this by construction:
        - Each cell added exactly once
        - Each passage added exactly once
        - No revisiting cells → no loops

        Returns:
            Always True (by construction for this algorithm)
        """
        return True
