# motors.py - Functions related to robot motor control


def move_forward(distance):
    """
    Command the robot to move forward.
    
    Args:
        distance: Distance to move in meters
    
    Returns:
        A status message
    """
    return f"Moving forward {distance} meters"


def turn(degrees):
    """
    Command the robot to turn.
    
    Args:
        degrees: Degrees to turn (positive = right, negative = left)
    
    Returns:
        A status message
    """
    direction = "right" if degrees > 0 else "left"
    return f"Turning {abs(degrees)} degrees {direction}"


def stop():
    """Emergency stop the robot."""
    return "Robot stopped!"

