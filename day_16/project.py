"""
🤖 Robot Environment Info Fetcher

This project teaches:
- Making API requests with the requests library
- Parsing JSON responses
- Error handling for network operations
- Making decisions based on external data

Your Task:
----------
Complete the functions below to fetch environmental data for robot decisions.

Note: For testing without internet, mock functions are provided.

1. fetch_weather_data(lat, lon)
   - Get weather from OpenWeatherMap API (or mock)

2. parse_weather_response(data)
   - Extract useful info from weather JSON

3. is_safe_for_outdoor_operation(weather_info)
   - Decide if robot should go outside

4. fetch_sunrise_sunset(lat, lon)
   - Get sunrise/sunset times

5. is_daytime(sunrise_sunset_info)
   - Check if it's currently daytime

6. get_robot_recommendation(lat, lon)
   - Combine all data into a recommendation

API Info:
---------
Weather: https://api.openweathermap.org/data/2.5/weather
Sunrise/Sunset: https://api.sunrise-sunset.org/json

For testing, use the mock functions that return sample data.
"""

import json
from datetime import datetime

# Try to import requests, but don't fail if not installed
try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False


# ============================================================
# MOCK DATA FOR TESTING (No API key needed)
# ============================================================

MOCK_WEATHER_SUNNY = {
    "weather": [{"main": "Clear", "description": "clear sky"}],
    "main": {"temp": 72, "humidity": 45},
    "wind": {"speed": 5},
    "name": "Test City"
}

MOCK_WEATHER_RAINY = {
    "weather": [{"main": "Rain", "description": "light rain"}],
    "main": {"temp": 55, "humidity": 90},
    "wind": {"speed": 15},
    "name": "Test City"
}

MOCK_WEATHER_EXTREME = {
    "weather": [{"main": "Thunderstorm", "description": "heavy thunderstorm"}],
    "main": {"temp": 45, "humidity": 95},
    "wind": {"speed": 35},
    "name": "Test City"
}

MOCK_SUNRISE_SUNSET = {
    "results": {
        "sunrise": "6:00:00 AM",
        "sunset": "8:00:00 PM",
        "solar_noon": "1:00:00 PM"
    },
    "status": "OK"
}


def get_mock_weather(condition="sunny"):
    """Get mock weather data for testing."""
    if condition == "rainy":
        return MOCK_WEATHER_RAINY.copy()
    elif condition == "extreme":
        return MOCK_WEATHER_EXTREME.copy()
    return MOCK_WEATHER_SUNNY.copy()


def get_mock_sunrise_sunset():
    """Get mock sunrise/sunset data for testing."""
    return MOCK_SUNRISE_SUNSET.copy()


# ============================================================
# YOUR FUNCTIONS TO IMPLEMENT
# ============================================================

def parse_weather_response(data):
    """
    Extract useful information from weather API response.
    
    Args:
        data: Dictionary from weather API (or mock data)
    
    Returns:
        A dictionary with parsed weather info:
        {
            "condition": main weather condition (e.g., "Clear", "Rain"),
            "description": detailed description,
            "temperature": temperature value,
            "humidity": humidity percentage,
            "wind_speed": wind speed,
            "location": city name
        }
    
    Example:
        parse_weather_response(MOCK_WEATHER_SUNNY)
        returns {"condition": "Clear", "temperature": 72, ...}
    """
    # TODO: Extract weather data from the response dictionary
    pass


def is_safe_for_outdoor_operation(weather_info):
    """
    Determine if weather conditions are safe for robot outdoor operation.
    
    Args:
        weather_info: Dictionary from parse_weather_response()
    
    Returns:
        Tuple of (is_safe: bool, reason: str)
    
    Safety Rules:
        - NOT safe if: Rain, Snow, Thunderstorm in condition
        - NOT safe if: wind_speed > 25
        - NOT safe if: temperature < 32 or temperature > 100
        - Safe otherwise
    
    Example:
        is_safe_for_outdoor_operation({"condition": "Rain", ...})
        returns (False, "Unsafe: Rain detected")
    """
    # TODO: Check weather conditions and return safety decision
    pass


def parse_sunrise_sunset_response(data):
    """
    Extract sunrise and sunset times from API response.
    
    Args:
        data: Dictionary from sunrise-sunset API (or mock)
    
    Returns:
        A dictionary with:
        {
            "sunrise": sunrise time string,
            "sunset": sunset time string,
            "status": "OK" or error status
        }
    
    Example:
        parse_sunrise_sunset_response(MOCK_SUNRISE_SUNSET)
        returns {"sunrise": "6:00:00 AM", "sunset": "8:00:00 PM", ...}
    """
    # TODO: Extract sunrise/sunset from response
    pass


def is_daytime(current_hour, sunrise_hour=6, sunset_hour=20):
    """
    Check if the current time is during daylight hours.
    
    Args:
        current_hour: Current hour (0-23)
        sunrise_hour: Hour of sunrise (default 6)
        sunset_hour: Hour of sunset (default 20)
    
    Returns:
        True if current_hour is between sunrise and sunset
    
    Example:
        is_daytime(14) -> True (2 PM is daytime)
        is_daytime(22) -> False (10 PM is night)
    """
    # TODO: Check if current hour is in daylight range
    pass


def get_operation_mode(weather_info, current_hour):
    """
    Determine the recommended operation mode based on conditions.
    
    Args:
        weather_info: Dictionary from parse_weather_response()
        current_hour: Current hour (0-23)
    
    Returns:
        A string with the recommended mode:
        - "outdoor_patrol" if safe and daytime
        - "indoor_tasks" if unsafe weather but daytime
        - "night_mode" if nighttime
        - "charging" if extreme conditions
    
    Example:
        get_operation_mode({"condition": "Clear", ...}, 14)
        returns "outdoor_patrol"
    """
    # TODO: Combine weather and time to recommend mode
    pass


def create_environment_report(weather_info, current_hour):
    """
    Create a comprehensive environment report for the robot.
    
    Args:
        weather_info: Dictionary from parse_weather_response()
        current_hour: Current hour (0-23)
    
    Returns:
        A dictionary with:
        {
            "timestamp": current hour,
            "weather_summary": brief weather description,
            "is_safe_outdoor": bool,
            "safety_reason": str,
            "is_daytime": bool,
            "recommended_mode": str,
            "alerts": list of any warnings
        }
    """
    # TODO: Compile all information into a report
    pass


def get_robot_recommendation(weather_condition="sunny", current_hour=12):
    """
    Get a complete recommendation for robot operation.
    
    This is the main function that combines everything.
    
    Args:
        weather_condition: "sunny", "rainy", or "extreme" (for mock data)
        current_hour: Current hour (0-23)
    
    Returns:
        A user-friendly string recommendation like:
        "Robot should: outdoor_patrol. Conditions: Clear, 72°F. Status: Safe for outdoor operation."
    """
    # TODO: Use all functions to generate a recommendation
    pass

