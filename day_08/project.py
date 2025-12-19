"""
🤖 Turtle Robot Grid Navigator

This project teaches:
- Coordinate systems (x, y)
- Event-driven programming concepts
- Movement and direction logic
- Boundary checking

Your Task:
----------
Complete the functions below that handle robot navigation logic.
These functions can later be connected to Turtle graphics for visualization.

1. create_robot_state(x, y, heading)
   - Create the initial state dictionary for a robot

2. move_forward(state, distance, grid_size)
   - Move robot forward, respecting grid boundaries

3. turn_left(state)
   - Rotate robot 90 degrees left

4. turn_right(state)
   - Rotate robot 90 degrees right

5. is_at_boundary(state, grid_size)
   - Check if robot is at the edge of the grid

6. get_path_history(state)
   - Return the robot's movement history

Grid System:
------------
- Grid is grid_size x grid_size (e.g., 400x400 pixels)
- Origin (0, 0) is at the center
- x increases going right, y increases going up
- Heading: 0=East, 90=North, 180=West, 270=South
"""


def create_robot_state(x=0, y=0, heading=0):
    """
    Create the initial state for a robot navigator.
    
    Args:
        x: Starting x coordinate (default 0)
        y: Starting y coordinate (default 0)
        heading: Starting direction in degrees (default 0 = East)
    
    Returns:
        A dictionary with robot state:
        {
            "x": x position,
            "y": y position,
            "heading": direction (0, 90, 180, or 270),
            "path": [(x, y)] - list of visited positions
        }
    
    Example:
        create_robot_state(0, 0, 90) returns:
        {"x": 0, "y": 0, "heading": 90, "path": [(0, 0)]}
    """
    # TODO: Create and return the state dictionary
    # Don't forget to initialize path with the starting position!
    pass


def move_forward(state, distance, grid_size=400):
    """
    Move the robot forward in its current heading direction.
    
    Args:
        state: The robot state dictionary
        distance: How far to move (integer)
        grid_size: The size of the grid (default 400)
    
    Returns:
        The updated state dictionary
    
    Rules:
        - Update x or y based on heading:
            - heading 0 (East): x += distance
            - heading 90 (North): y += distance
            - heading 180 (West): x -= distance
            - heading 270 (South): y -= distance
        - Keep robot within bounds: -grid_size/2 to +grid_size/2
        - Add new position to path history
    
    Example:
        state = {"x": 0, "y": 0, "heading": 0, "path": [(0,0)]}
        move_forward(state, 50, 400) -> x becomes 50
    """
    # TODO: Calculate new position based on heading
    # TODO: Clamp position to grid boundaries
    # TODO: Update state and add to path
    pass


def turn_left(state):
    """
    Rotate the robot 90 degrees counter-clockwise.
    
    Args:
        state: The robot state dictionary
    
    Returns:
        The updated state dictionary
    
    Heading changes:
        0 -> 90, 90 -> 180, 180 -> 270, 270 -> 0
    
    Example:
        state["heading"] = 0
        turn_left(state)
        state["heading"] -> 90
    """
    # TODO: Add 90 to heading and use modulo 360
    pass


def turn_right(state):
    """
    Rotate the robot 90 degrees clockwise.
    
    Args:
        state: The robot state dictionary
    
    Returns:
        The updated state dictionary
    
    Heading changes:
        0 -> 270, 90 -> 0, 180 -> 90, 270 -> 180
    
    Example:
        state["heading"] = 0
        turn_right(state)
        state["heading"] -> 270
    """
    # TODO: Subtract 90 from heading and use modulo 360
    pass


def is_at_boundary(state, grid_size=400):
    """
    Check if the robot is at or near the edge of the grid.
    
    Args:
        state: The robot state dictionary
        grid_size: The size of the grid (default 400)
    
    Returns:
        True if robot is within 10 units of any boundary, False otherwise
    
    Boundaries are at ±grid_size/2 for both x and y.
    
    Example:
        state = {"x": 195, "y": 0, ...}  # grid_size=400
        is_at_boundary(state, 400) -> True (195 is close to 200)
    """
    # TODO: Check if x or y is within 10 of the boundary
    pass


def get_path_history(state):
    """
    Return a copy of the robot's path history.
    
    Args:
        state: The robot state dictionary
    
    Returns:
        A list of (x, y) tuples representing visited positions
    
    Example:
        state["path"] = [(0, 0), (50, 0), (50, 50)]
        get_path_history(state) -> [(0, 0), (50, 0), (50, 50)]
    """
    # TODO: Return a copy of state["path"]
    pass


def calculate_total_distance(state):
    """
    Calculate the total distance traveled by the robot.
    
    Args:
        state: The robot state dictionary
    
    Returns:
        Total distance as a float (sum of distances between consecutive points)
    
    Formula for distance between two points:
        sqrt((x2-x1)² + (y2-y1)²)
    
    Example:
        path = [(0, 0), (3, 0), (3, 4)]
        # Distance: 3 + 4 = 7
        calculate_total_distance(state) -> 7.0
    """
    # TODO: Loop through path and sum distances between consecutive points
    pass

