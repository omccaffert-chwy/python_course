"""
🤖 Debug the Broken Robot Script

This project teaches:
- Debugging techniques
- Using print statements to trace execution
- Identifying common bug types
- Fixing logical errors

YOUR TASK:
----------
This script has BUGS! Find and fix them.

The robot should:
1. Move forward the specified distance
2. Turn by the specified degrees (positive = left, negative = right)
3. Track total distance traveled
4. Report position correctly

BUGS TO FIND:
- Off-by-one errors
- Wrong operators
- Logic errors
- Variable scope issues
- Type errors

After fixing, all tests in tests.py should pass!

DEBUGGING TIPS:
- Add print() statements to see variable values
- Check each calculation step by step
- Compare expected vs actual output
- Use the debugger to step through code
"""

import math


class BuggyRobot:
    """A robot class with several bugs to fix."""
    
    def __init__(self, name):
        """Initialize the robot."""
        self.name = name
        self.x = 0
        self.y = 0
        self.heading = 0  # degrees, 0 = facing right/east
        self.total_distance = 0
        # BUG 1: Something wrong with the history initialization
        self.position_history = (0, 0)
    
    def move(self, distance):
        """
        Move the robot forward by 'distance' units.
        
        The robot moves in the direction it's facing (self.heading).
        heading 0 = east (+x), 90 = north (+y), etc.
        """
        # Convert heading to radians for trig functions
        # BUG 2: Wrong conversion formula
        radians = self.heading * 180 / math.pi
        
        # Calculate new position
        # BUG 3: Trig functions might be swapped
        dx = distance * math.sin(radians)
        dy = distance * math.cos(radians)
        
        self.x += dx
        self.y += dy
        
        # Track total distance
        # BUG 4: Wrong operator
        self.total_distance -= distance
        
        # Add to history
        # BUG 5: Using wrong method for list
        self.position_history.add((self.x, self.y))
    
    def turn(self, degrees):
        """
        Turn the robot by 'degrees'.
        Positive = counter-clockwise (left)
        Negative = clockwise (right)
        """
        # BUG 6: Should add, not subtract
        self.heading = self.heading - degrees
        
        # Keep heading in 0-359 range
        # BUG 7: Wrong modulo value
        self.heading = self.heading % 180
    
    def get_position(self):
        """Return current (x, y) position rounded to 2 decimal places."""
        # BUG 8: Only rounding x
        return (round(self.x, 2), self.y)
    
    def get_distance_from_origin(self):
        """Calculate distance from starting point (0, 0)."""
        # BUG 9: Wrong formula (should be sqrt of sum of squares)
        return math.sqrt(self.x + self.y)
    
    def get_status(self):
        """Return a status string."""
        # BUG 10: f-string formatting error
        return f"Robot {name}: Position {self.get_position()}, Heading {self.heading}°"


def calculate_path_length(positions):
    """
    Calculate the total length of a path through positions.
    
    Args:
        positions: List of (x, y) tuples
    
    Returns:
        Total distance traveled
    """
    if len(positions) < 2:
        return 0
    
    total = 0
    # BUG 11: Loop range is wrong (off by one)
    for i in range(len(positions)):
        x1, y1 = positions[i]
        x2, y2 = positions[i + 1]
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        total += distance
    
    return total


def count_turns(commands):
    """
    Count the number of turn commands in a list.
    
    Args:
        commands: List of command strings like ["F10", "L90", "R45"]
    
    Returns:
        Number of turns (L or R commands)
    """
    count = 0
    for cmd in commands:
        # BUG 12: Wrong comparison (should check first character)
        if cmd == "L" or cmd == "R":
            count += 1
    return count


def find_furthest_position(positions):
    """
    Find the position furthest from the origin.
    
    Args:
        positions: List of (x, y) tuples
    
    Returns:
        The (x, y) tuple furthest from (0, 0)
    """
    if not positions:
        return None
    
    furthest = positions[0]
    max_distance = 0  # BUG 13: Should start with first position's distance
    
    for pos in positions:
        x, y = pos
        distance = math.sqrt(x**2 + y**2)
        # BUG 14: Wrong comparison operator
        if distance < max_distance:
            max_distance = distance
            furthest = pos
    
    return furthest


# ============================================================
# FIXED VERSIONS - Students should make their fixes match these
# (This section is for reference - delete when giving to students)
# ============================================================

class FixedRobot:
    """The corrected version of the robot class."""
    
    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.heading = 0
        self.total_distance = 0
        self.position_history = [(0, 0)]  # FIX 1: Use list
    
    def move(self, distance):
        # FIX 2: Correct conversion
        radians = self.heading * math.pi / 180
        
        # FIX 3: cos for x, sin for y
        dx = distance * math.cos(radians)
        dy = distance * math.sin(radians)
        
        self.x += dx
        self.y += dy
        
        # FIX 4: Should add
        self.total_distance += distance
        
        # FIX 5: Use append for list
        self.position_history.append((self.x, self.y))
    
    def turn(self, degrees):
        # FIX 6: Should add
        self.heading = self.heading + degrees
        # FIX 7: Modulo 360
        self.heading = self.heading % 360
    
    def get_position(self):
        # FIX 8: Round both
        return (round(self.x, 2), round(self.y, 2))
    
    def get_distance_from_origin(self):
        # FIX 9: Square the values
        return math.sqrt(self.x**2 + self.y**2)
    
    def get_status(self):
        # FIX 10: self.name
        return f"Robot {self.name}: Position {self.get_position()}, Heading {self.heading}°"

