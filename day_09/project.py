"""
🤖 Robot Parts Collection Game

This project teaches:
- Game state management
- Collision detection
- Lists for tracking segments/history
- Score tracking
- Game loop logic

Your Task:
----------
Complete the functions below to build a parts collection game.
The robot collects parts while avoiding walls and its own trail.

1. create_game_state(grid_size, start_pos)
   - Initialize the game state

2. spawn_part(state)
   - Place a new collectible part at a random location

3. move_robot(state, direction)
   - Move the robot and update the trail

4. check_wall_collision(state)
   - Check if robot hit a wall

5. check_trail_collision(state)
   - Check if robot hit its own trail

6. check_part_collection(state)
   - Check if robot collected a part

7. update_game(state, direction)
   - Main game update function combining all logic

Game Rules:
-----------
- Robot moves on a grid, leaving a trail behind
- Collect parts to increase score
- Hitting a wall = game over
- Hitting your own trail = game over
- Each part collected adds to score and grows the trail
"""

import random


def create_game_state(grid_size=20, start_pos=None):
    """
    Create the initial game state.
    
    Args:
        grid_size: Size of the grid (grid_size x grid_size)
        start_pos: Starting (x, y) tuple, default is center
    
    Returns:
        A dictionary with game state:
        {
            "grid_size": size of the grid,
            "robot_pos": (x, y) current position,
            "trail": [(x, y), ...] list of visited positions,
            "part_pos": (x, y) or None if no part spawned,
            "score": current score,
            "game_over": False,
            "direction": "right" (current direction)
        }
    
    Example:
        state = create_game_state(20)
        state["robot_pos"] -> (10, 10)  # center of 20x20 grid
    """
    # TODO: Create and return the game state dictionary
    # Default start_pos should be center: (grid_size // 2, grid_size // 2)
    pass


def spawn_part(state):
    """
    Spawn a new collectible part at a random empty location.
    
    Args:
        state: The game state dictionary
    
    Returns:
        The updated state with a new part_pos
    
    Rules:
        - Part must not spawn on the robot's current position
        - Part must not spawn on the trail
        - Part position must be within grid bounds (0 to grid_size-1)
    
    Example:
        spawn_part(state)
        state["part_pos"] -> (5, 12)  # random position
    """
    # TODO: Generate random x, y that's not on robot or trail
    # Hint: Use a while loop to keep trying until valid position found
    pass


def move_robot(state, direction):
    """
    Move the robot one step in the given direction.
    
    Args:
        state: The game state dictionary
        direction: "up", "down", "left", or "right"
    
    Returns:
        The updated state with new robot position
    
    Movement:
        - "up": y += 1
        - "down": y -= 1
        - "left": x -= 1
        - "right": x += 1
    
    Also:
        - Add old position to trail
        - Update state["direction"]
    
    Example:
        state["robot_pos"] = (10, 10)
        move_robot(state, "right")
        state["robot_pos"] -> (11, 10)
    """
    # TODO: Calculate new position based on direction
    # TODO: Add old position to trail
    # TODO: Update robot_pos and direction
    pass


def check_wall_collision(state):
    """
    Check if the robot has collided with a wall.
    
    Args:
        state: The game state dictionary
    
    Returns:
        True if robot is outside grid bounds, False otherwise
    
    Walls are at:
        x < 0 or x >= grid_size
        y < 0 or y >= grid_size
    
    Example:
        state["robot_pos"] = (-1, 5)
        check_wall_collision(state) -> True
    """
    # TODO: Check if robot_pos is outside bounds
    pass


def check_trail_collision(state):
    """
    Check if the robot has collided with its own trail.
    
    Args:
        state: The game state dictionary
    
    Returns:
        True if robot position is in the trail, False otherwise
    
    Example:
        state["robot_pos"] = (5, 5)
        state["trail"] = [(5, 5), (6, 5)]
        check_trail_collision(state) -> True
    """
    # TODO: Check if robot_pos is in trail list
    pass


def check_part_collection(state):
    """
    Check if the robot has collected a part.
    
    Args:
        state: The game state dictionary
    
    Returns:
        True if robot is on the part, False otherwise
    
    If collected:
        - Increment score by 10
        - Set part_pos to None (will need to spawn new one)
    
    Example:
        state["robot_pos"] = (5, 5)
        state["part_pos"] = (5, 5)
        check_part_collection(state) -> True
        state["score"] -> 10
    """
    # TODO: Check if robot_pos equals part_pos
    # TODO: If so, increase score and clear part_pos
    pass


def update_game(state, direction):
    """
    Main game update function - runs one game tick.
    
    Args:
        state: The game state dictionary
        direction: The direction to move
    
    Returns:
        The updated state
    
    Order of operations:
        1. Move the robot
        2. Check wall collision -> game_over = True
        3. Check trail collision -> game_over = True
        4. Check part collection -> increase score
        5. If no part exists, spawn one
    
    Example:
        update_game(state, "right")
        # Robot moves, collisions checked, parts collected
    """
    # TODO: Implement the game update logic in order
    pass


def get_game_summary(state):
    """
    Generate a summary of the current game state.
    
    Args:
        state: The game state dictionary
    
    Returns:
        A string summary like:
        "Score: 30 | Position: (15, 10) | Trail length: 4 | Status: Playing"
        or "Status: Game Over" if game_over is True
    """
    # TODO: Return a formatted game summary string
    pass

