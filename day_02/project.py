"""
🤖 Robot Safety Check System

This project teaches:
- Conditionals (if/elif/else)
- Comparison operators (==, !=, <, >, <=, >=)
- Logical operators (and, or, not)
- String methods (.lower(), .strip())
- Nested conditionals

Your Task:
----------
Complete the five functions below:

1. normalize_input(text)
   - Clean up user input by removing whitespace and converting to lowercase

2. check_battery_level(level)
   - Determine if battery is sufficient to operate

3. check_sensor_status(status)
   - Determine if sensors are operational

4. check_operation_mode(mode)
   - Determine which operation mode to activate

5. get_startup_result(battery_level, sensor_status, operation_mode)
   - Run the full startup sequence and return the result

Robot Startup Sequence:
-----------------------
Check 1: Battery Level (number)
  - >= 20 → continue to Check 2
  - < 20 → "Battery critical. Shutting down."

Check 2: Sensor Status ("online" or other)
  - "online" → continue to Check 3
  - anything else → "Sensors offline. Cannot operate safely."

Check 3: Operation Mode ("patrol", "charge", "maintenance", or other)
  - "patrol" → "Patrol mode activated. Robot operational."
  - "charge" → "Returning to charging station."
  - "maintenance" → "Maintenance mode. Motors disabled."
  - anything else → "Unknown mode. Standby activated."
"""


def normalize_input(text):
    """
    Clean up user input for consistent comparison.
    
    Args:
        text: Raw input string from user
    
    Returns:
        Cleaned string (lowercase, no leading/trailing whitespace)
    
    Examples:
        normalize_input("  ONLINE  ") should return "online"
        normalize_input("PATROL") should return "patrol"
    """
    # TODO: Use .strip() and .lower() to clean the input
    pass


def check_battery_level(level):
    """
    Evaluate if battery level is sufficient for operation.
    
    Args:
        level: Battery percentage as an integer (0-100)
    
    Returns:
        True if level >= 20 (safe to operate)
        False if level < 20 (critical, must shut down)
    
    Examples:
        check_battery_level(50) should return True
        check_battery_level(15) should return False
        check_battery_level(20) should return True
    """
    # TODO: Return True if level >= 20, False otherwise
    pass


def check_sensor_status(status):
    """
    Evaluate if sensors are operational.
    
    Args:
        status: The sensor status (should already be normalized)
    
    Returns:
        True if status is "online" (sensors working)
        False if status is anything else (sensors not working)
    
    Examples:
        check_sensor_status("online") should return True
        check_sensor_status("offline") should return False
        check_sensor_status("error") should return False
    """
    # TODO: Return True if status is "online", False otherwise
    pass


def check_operation_mode(mode):
    """
    Determine which operation mode to activate.
    
    Args:
        mode: The requested operation mode (should already be normalized)
    
    Returns:
        A string describing the mode:
        - "patrol" if mode is "patrol"
        - "charge" if mode is "charge"
        - "maintenance" if mode is "maintenance"
        - "standby" for any other mode
    
    Examples:
        check_operation_mode("patrol") should return "patrol"
        check_operation_mode("charge") should return "charge"
        check_operation_mode("maintenance") should return "maintenance"
        check_operation_mode("dance") should return "standby"
    """
    # TODO: Use if/elif/else to return the correct mode
    pass


def get_startup_result(battery_level, sensor_status, operation_mode):
    """
    Run the full robot startup sequence and return the result.
    
    This function should:
    1. Check battery level using check_battery_level()
    2. Normalize and check sensor status using check_sensor_status()
    3. Normalize and check operation mode using check_operation_mode()
    
    Args:
        battery_level: Battery percentage as an integer
        sensor_status: Sensor status string
        operation_mode: Requested operation mode string
    
    Returns:
        A string with the startup result message:
        - "Battery critical. Shutting down."
        - "Sensors offline. Cannot operate safely."
        - "Patrol mode activated. Robot operational."
        - "Returning to charging station."
        - "Maintenance mode. Motors disabled."
        - "Unknown mode. Standby activated."
    
    Examples:
        get_startup_result(50, "online", "patrol") returns "Patrol mode activated. Robot operational."
        get_startup_result(10, "online", "patrol") returns "Battery critical. Shutting down."
        get_startup_result(50, "offline", "patrol") returns "Sensors offline. Cannot operate safely."
    """
    # TODO: Check battery_level using check_battery_level()
    # If False, return the battery critical message
    
    # TODO: Normalize sensor_status and check using check_sensor_status()
    # If False, return the sensors offline message
    
    # TODO: Normalize operation_mode and check using check_operation_mode()
    # Return the appropriate message based on the mode
    
    pass
