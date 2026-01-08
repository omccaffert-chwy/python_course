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

2. battery_level_OK(level)
   - Determine if battery is sufficient to operate

3. sensor_status_online(status)
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
    input_text = text
    normalize_input = input_text.lower()
    normalize_input = normalize_input.strip()
    return normalize_input 
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
        battery_level_OK(50) should return True
        battery_level_OK(15) should return False
        battery_level_OK(20) should return True
    """
    # TODO: Return True if level >= 20, False otherwise
    battery_level = level
    battery_level_OK = False
    if battery_level >= 20:
        battery_level_OK = True
    else:
        battery_level_OK = False
    
    return battery_level_OK

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
        sensor_status_online("online") should return True
        sensor_status_online("offline") should return False
        sensor_status_online("error") should return False
    """
    # TODO: Return True if status is "online", False otherwise
    sensor_status = status.lower()
    sensor_status_online = True
    if sensor_status == "online":
        sensor_status_online = True
    else:
        sensor_status_online = False

    return sensor_status_online
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
    operation_mode = mode.lower()
    if operation_mode == "dance":
        operation_mode = "standby"
    else:
        return operation_mode
    return operation_mode
    pass


def get_startup_result(battery_level, sensor_status, operation_mode):
    """
    Run the full robot startup sequence and return the result.
    
    This function should:
    1. Check battery level using battery_level_OK()
    2. Normalize and check sensor status using sensor_status_online()
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
    # TODO: Check battery_level using battery_level_OK()
    # If False, return the battery critical message
    
    # TODO: Normalize sensor_status and check using sensor_status_online()
    # If False, return the sensors offline message
    
    # TODO: Normalize operation_mode and check using check_operation_mode()
    # Return the appropriate message based on the mode

    result_message = ""
    #Check battery
    battery_level_OK = check_battery_level(battery_level)
    if battery_level_OK == False:
        result_message = "Battery critical. Shutting down"
        return result_message
    #Check sensor online
    sensor_status_online = check_sensor_status(sensor_status)
    if sensor_status_online == False: 
        result_message = "Sensors offline. Cannot operate safely."
        return result_message
    #Check operational mode
    operation_mode = check_operation_mode(operation_mode)
    if operation_mode == "patrol":
        result_message = "Patrol mode activated. Robot operational."
    elif operation_mode == "charge":
        result_message = "Returning to charging station."
    elif operation_mode == "maintenance":
        result_message = "Maintenance mode. Motors disabled."
    else:
        result_message = "Unknown mode. Standby activated."

    return result_message
    pass
