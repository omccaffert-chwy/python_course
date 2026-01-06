# sensors.py - Functions related to robot sensors


def get_sensor_reading(sensor_name):
    """
    Simulate getting a reading from a sensor.
    
    Args:
        sensor_name: Name of the sensor (e.g., "lidar", "camera", "ultrasonic")
    
    Returns:
        A simulated sensor reading
    """
    readings = {
        "lidar": 5.2,
        "camera": "frame_captured",
        "ultrasonic": 1.8,
        "temperature": 23.5,
    }
    return readings.get(sensor_name, "unknown sensor")


def list_available_sensors():
    """Return a list of available sensor names."""
    return ["lidar", "camera", "ultrasonic", "temperature"]


# Try adding your own sensor function here!

