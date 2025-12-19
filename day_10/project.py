"""
🤖 Robot Mission Log

This project teaches:
- File reading with open() and read modes
- File writing with write and append modes
- Using 'with' statement for safe file handling
- Parsing and formatting text data

Your Task:
----------
Complete the functions below to create a mission logging system.

1. create_mission_entry(mission_id, tasks_completed, energy_used, success)
   - Create a formatted log entry string

2. append_mission_log(filename, entry)
   - Append a mission entry to a log file

3. read_mission_log(filename)
   - Read all entries from a log file

4. get_last_n_missions(filename, n)
   - Get the last n missions from the log

5. calculate_success_rate(filename)
   - Calculate mission success rate from log

6. get_mission_statistics(filename)
   - Get comprehensive statistics from log

Log Format:
-----------
Each line in the log file is formatted as:
MISSION_ID|TASKS_COMPLETED|ENERGY_USED|SUCCESS

Example:
M001|5|75|True
M002|3|45|False
M003|7|90|True
"""


def create_mission_entry(mission_id, tasks_completed, energy_used, success):
    """
    Create a formatted mission log entry.
    
    Args:
        mission_id: Unique mission identifier (string, e.g., "M001")
        tasks_completed: Number of tasks completed (integer)
        energy_used: Energy consumed (integer)
        success: Whether mission succeeded (boolean)
    
    Returns:
        A formatted string: "MISSION_ID|TASKS|ENERGY|SUCCESS"
    
    Example:
        create_mission_entry("M001", 5, 75, True)
        returns "M001|5|75|True"
    """
    # TODO: Return formatted string with pipe separators
    pass


def append_mission_log(filename, entry):
    """
    Append a mission entry to the log file.
    
    Args:
        filename: Path to the log file
        entry: The formatted entry string to append
    
    Returns:
        True if successful, False if an error occurred
    
    Notes:
        - Use 'a' mode to append
        - Add a newline after the entry
        - Use 'with' statement for safe file handling
    
    Example:
        append_mission_log("missions.txt", "M001|5|75|True")
        # File now contains: M001|5|75|True\n
    """
    # TODO: Open file in append mode and write entry + newline
    pass


def read_mission_log(filename):
    """
    Read all mission entries from the log file.
    
    Args:
        filename: Path to the log file
    
    Returns:
        A list of entry strings (without newlines)
        Returns empty list if file doesn't exist
    
    Example:
        read_mission_log("missions.txt")
        returns ["M001|5|75|True", "M002|3|45|False"]
    """
    # TODO: Read file and return list of lines
    # Handle FileNotFoundError by returning empty list
    pass


def parse_mission_entry(entry):
    """
    Parse a mission entry string into its components.
    
    Args:
        entry: A formatted entry string "ID|TASKS|ENERGY|SUCCESS"
    
    Returns:
        A dictionary with parsed values:
        {
            "mission_id": string,
            "tasks_completed": int,
            "energy_used": int,
            "success": bool
        }
    
    Example:
        parse_mission_entry("M001|5|75|True")
        returns {"mission_id": "M001", "tasks_completed": 5, 
                 "energy_used": 75, "success": True}
    """
    # TODO: Split the entry and convert to appropriate types
    pass


def get_last_n_missions(filename, n):
    """
    Get the last n missions from the log.
    
    Args:
        filename: Path to the log file
        n: Number of missions to retrieve
    
    Returns:
        A list of the last n parsed mission dictionaries
        (most recent last)
    
    Example:
        # Log has M001, M002, M003
        get_last_n_missions("missions.txt", 2)
        returns [parsed_M002, parsed_M003]
    """
    # TODO: Read log, parse entries, return last n
    pass


def calculate_success_rate(filename):
    """
    Calculate the mission success rate from the log.
    
    Args:
        filename: Path to the log file
    
    Returns:
        Success rate as a float between 0.0 and 1.0
        Returns 0.0 if no missions in log
    
    Example:
        # Log has 10 missions, 7 successful
        calculate_success_rate("missions.txt")
        returns 0.7
    """
    # TODO: Read all missions, count successes, calculate rate
    pass


def get_mission_statistics(filename):
    """
    Get comprehensive statistics from the mission log.
    
    Args:
        filename: Path to the log file
    
    Returns:
        A dictionary with statistics:
        {
            "total_missions": int,
            "successful_missions": int,
            "failed_missions": int,
            "success_rate": float,
            "total_tasks": int,
            "total_energy": int,
            "avg_tasks_per_mission": float,
            "avg_energy_per_mission": float
        }
    
    Returns dict with all zeros if log is empty.
    """
    # TODO: Calculate all statistics from the log
    pass


def clear_mission_log(filename):
    """
    Clear all entries from the mission log.
    
    Args:
        filename: Path to the log file
    
    Returns:
        True if successful
    
    Note: Use 'w' mode which overwrites/creates empty file
    """
    # TODO: Open file in write mode to clear it
    pass

