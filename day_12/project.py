"""
🤖 Robot Command Translator

This project teaches:
- List comprehensions
- Dictionary comprehensions
- String parsing and manipulation
- Iterating over data structures

Your Task:
----------
Complete the functions below to translate robot commands.

Command Format:
---------------
Commands are short codes like:
- F10 = Move Forward 10 units
- B5 = Move Backward 5 units
- L90 = Turn Left 90 degrees
- R45 = Turn Right 45 degrees
- W3 = Wait 3 seconds
- S = Stop

1. parse_command(cmd)
   - Parse a single command into action and value

2. translate_command(cmd)
   - Convert command code to human-readable string

3. parse_command_sequence(sequence)
   - Parse a string of multiple commands

4. translate_sequence(commands)
   - Translate a list of commands to readable descriptions

5. commands_to_dict(commands)
   - Convert commands to dictionary using comprehension

6. filter_movement_commands(commands)
   - Use comprehension to filter only movement commands

7. calculate_total_distance(commands)
   - Sum all forward/backward movement distances
"""


def parse_command(cmd):
    """
    Parse a single command into its action and value.
    
    Args:
        cmd: A command string like "F10", "L90", "S"
    
    Returns:
        A tuple of (action, value) where:
        - action is the letter(s) (string)
        - value is the number (integer) or 0 if no number
    
    Examples:
        parse_command("F10") -> ("F", 10)
        parse_command("L90") -> ("L", 90)
        parse_command("S") -> ("S", 0)
    
    Hint: Use string slicing and isdigit()
    """
    # TODO: Separate the letter(s) from the number
    pass


def translate_command(cmd):
    """
    Convert a command code to human-readable string.
    
    Args:
        cmd: A command string like "F10"
    
    Returns:
        A human-readable description string
    
    Translation:
        F = "Move forward X units"
        B = "Move backward X units"
        L = "Turn left X degrees"
        R = "Turn right X degrees"
        W = "Wait X seconds"
        S = "Stop"
    
    Examples:
        translate_command("F10") -> "Move forward 10 units"
        translate_command("L90") -> "Turn left 90 degrees"
        translate_command("S") -> "Stop"
    """
    # TODO: Parse command and return appropriate description
    pass


def parse_command_sequence(sequence):
    """
    Parse a string of multiple commands separated by spaces.
    
    Args:
        sequence: A string like "F10 L90 F5 R45 S"
    
    Returns:
        A list of individual command strings
    
    Example:
        parse_command_sequence("F10 L90 F5")
        returns ["F10", "L90", "F5"]
    
    Hint: Use split()
    """
    # TODO: Split the sequence into individual commands
    pass


def translate_sequence(commands):
    """
    Translate a list of commands to readable descriptions.
    
    Args:
        commands: A list of command strings
    
    Returns:
        A list of human-readable descriptions
    
    Example:
        translate_sequence(["F10", "L90"])
        returns ["Move forward 10 units", "Turn left 90 degrees"]
    
    USE A LIST COMPREHENSION!
    """
    # TODO: Use a list comprehension to translate all commands
    pass


def commands_to_dict(commands):
    """
    Convert a list of commands to a dictionary with index keys.
    
    Args:
        commands: A list of command strings
    
    Returns:
        A dictionary where keys are step numbers (1, 2, 3...)
        and values are the commands
    
    Example:
        commands_to_dict(["F10", "L90", "F5"])
        returns {1: "F10", 2: "L90", 3: "F5"}
    
    USE A DICT COMPREHENSION with enumerate()!
    """
    # TODO: Use a dict comprehension to create the mapping
    pass


def filter_movement_commands(commands):
    """
    Filter to only forward and backward movement commands.
    
    Args:
        commands: A list of command strings
    
    Returns:
        A list containing only F and B commands
    
    Example:
        filter_movement_commands(["F10", "L90", "B5", "R45", "F3"])
        returns ["F10", "B5", "F3"]
    
    USE A LIST COMPREHENSION with a condition!
    """
    # TODO: Use a list comprehension to filter F and B commands
    pass


def filter_turn_commands(commands):
    """
    Filter to only turn commands (L and R).
    
    Args:
        commands: A list of command strings
    
    Returns:
        A list containing only L and R commands
    
    Example:
        filter_turn_commands(["F10", "L90", "B5", "R45"])
        returns ["L90", "R45"]
    
    USE A LIST COMPREHENSION!
    """
    # TODO: Use a list comprehension to filter L and R commands
    pass


def calculate_total_distance(commands):
    """
    Calculate total forward distance (F adds, B subtracts).
    
    Args:
        commands: A list of command strings
    
    Returns:
        Net distance as an integer (F positive, B negative)
    
    Example:
        calculate_total_distance(["F10", "L90", "B3", "F5"])
        returns 12 (10 - 3 + 5)
    
    Hint: Use parse_command to extract values
    """
    # TODO: Sum F values and subtract B values
    pass


def get_command_summary(commands):
    """
    Generate a summary of command types using comprehensions.
    
    Args:
        commands: A list of command strings
    
    Returns:
        A dictionary with counts of each command type:
        {"F": count, "B": count, "L": count, "R": count, "W": count, "S": count}
    
    Example:
        get_command_summary(["F10", "F5", "L90", "R45"])
        returns {"F": 2, "B": 0, "L": 1, "R": 1, "W": 0, "S": 0}
    """
    # TODO: Count each command type
    pass

