"""
🤖 Pathfinding on a Grid

This project teaches:
- 2D grid representation
- Breadth-First Search (BFS) algorithm
- Algorithm thinking and Big-O concepts
- Path visualization

Your Task:
----------
Complete the functions below to implement grid pathfinding.

1. create_grid(width, height)
   - Create an empty grid

2. add_obstacle(grid, x, y)
   - Mark a cell as blocked

3. is_valid_cell(grid, x, y)
   - Check if a cell can be visited

4. get_neighbors(grid, x, y)
   - Get all valid adjacent cells

5. find_path_bfs(grid, start, goal)
   - Find shortest path using BFS

6. visualize_grid(grid, path)
   - Create a string visualization

Grid Representation:
--------------------
- 0 = empty cell (can walk)
- 1 = obstacle (blocked)
- Grid is a list of lists: grid[y][x]

Coordinates:
- (0, 0) is top-left
- x increases going right
- y increases going down
"""

from collections import deque


def create_grid(width, height, fill=0):
    """
    Create a 2D grid of the specified size.
    
    Args:
        width: Number of columns
        height: Number of rows
        fill: Value to fill cells with (default 0)
    
    Returns:
        A 2D list (list of lists) representing the grid
        Access with grid[y][x]
    
    Example:
        grid = create_grid(5, 3)
        # Creates a 5x3 grid of zeros
        # grid[0] is the first row with 5 cells
    """
    # TODO: Create and return the 2D grid
    pass


def add_obstacle(grid, x, y):
    """
    Mark a cell as an obstacle (blocked).
    
    Args:
        grid: The 2D grid
        x: Column index
        y: Row index
    
    Returns:
        The modified grid
    
    Example:
        add_obstacle(grid, 2, 1)  # Block cell at column 2, row 1
    """
    # TODO: Set grid[y][x] to 1 (obstacle)
    pass


def is_valid_cell(grid, x, y):
    """
    Check if a cell is valid to visit.
    
    Args:
        grid: The 2D grid
        x: Column index
        y: Row index
    
    Returns:
        True if:
        - x and y are within grid bounds
        - Cell is not an obstacle (value != 1)
        False otherwise
    
    Example:
        is_valid_cell(grid, 2, 1) -> True/False
    """
    # TODO: Check bounds and obstacle status
    pass


def get_neighbors(grid, x, y):
    """
    Get all valid neighboring cells (up, down, left, right).
    
    Args:
        grid: The 2D grid
        x: Current column
        y: Current row
    
    Returns:
        A list of (x, y) tuples for valid neighbors
    
    Only returns cells that pass is_valid_cell().
    Does NOT include diagonal neighbors.
    
    Example:
        get_neighbors(grid, 1, 1)
        might return [(0,1), (2,1), (1,0), (1,2)]
    """
    # TODO: Check all 4 directions and return valid neighbors
    pass


def find_path_bfs(grid, start, goal):
    """
    Find the shortest path from start to goal using BFS.
    
    Args:
        grid: The 2D grid
        start: Starting position (x, y) tuple
        goal: Goal position (x, y) tuple
    
    Returns:
        A list of (x, y) tuples representing the path from start to goal
        Returns empty list if no path exists
    
    BFS Algorithm:
        1. Create a queue with start position
        2. Track visited cells and parent of each cell
        3. While queue not empty:
            - Get next cell from queue
            - If it's the goal, reconstruct path
            - Otherwise, add unvisited neighbors to queue
        4. If queue empties without finding goal, no path exists
    
    Example:
        path = find_path_bfs(grid, (0, 0), (4, 4))
        # Returns [(0,0), (1,0), (2,0), ...] or [] if blocked
    """
    # TODO: Implement BFS pathfinding
    pass


def reconstruct_path(came_from, start, goal):
    """
    Reconstruct the path from start to goal using the came_from dict.
    
    Args:
        came_from: Dictionary mapping each cell to its parent
        start: Starting position (x, y)
        goal: Goal position (x, y)
    
    Returns:
        List of positions from start to goal
    
    Example:
        came_from = {(1,0): (0,0), (2,0): (1,0)}
        reconstruct_path(came_from, (0,0), (2,0))
        returns [(0,0), (1,0), (2,0)]
    """
    # TODO: Walk backwards from goal to start, then reverse
    pass


def calculate_path_length(path):
    """
    Calculate the length of a path (number of steps).
    
    Args:
        path: List of (x, y) positions
    
    Returns:
        Number of steps (length - 1, since start doesn't count as a step)
    
    Example:
        calculate_path_length([(0,0), (1,0), (2,0)])
        returns 2
    """
    # TODO: Return the number of steps
    pass


def visualize_grid(grid, path=None, start=None, goal=None):
    """
    Create a string visualization of the grid.
    
    Args:
        grid: The 2D grid
        path: Optional list of path positions to highlight
        start: Optional start position to mark
        goal: Optional goal position to mark
    
    Returns:
        A multi-line string showing the grid:
        - '.' for empty cells
        - '#' for obstacles
        - '*' for path cells
        - 'S' for start
        - 'G' for goal
    
    Example:
        . . # . .
        . * # . .
        S * * * G
    """
    # TODO: Build and return the visualization string
    pass


def count_reachable_cells(grid, start):
    """
    Count how many cells are reachable from the start position.
    
    Args:
        grid: The 2D grid
        start: Starting position (x, y)
    
    Returns:
        Number of cells that can be reached from start
    
    Hint: Use BFS but count visited cells instead of finding path
    """
    # TODO: Use BFS to count reachable cells
    pass

