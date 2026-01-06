"""
main.py - Demonstrates importing from a Python package

Run this file from the day_06 directory:
    python main.py

This shows different ways to import from the robot_package.
"""

print("=" * 50)
print("Demonstrating Python Package Imports")
print("=" * 50)
print()

# Method 1: Import specific functions from the package
# (These work because __init__.py exposes them)
from robot_package import get_sensor_reading, move_forward

print("Method 1: Import from package directly")
print(f"  Sensor reading: {get_sensor_reading('lidar')}")
print(f"  Motor command: {move_forward(2.5)}")
print()

# Method 2: Import from specific modules
from robot_package.sensors import list_available_sensors
from robot_package.motors import turn, stop

print("Method 2: Import from specific modules")
print(f"  Available sensors: {list_available_sensors()}")
print(f"  Turn command: {turn(90)}")
print(f"  Stop command: {stop()}")
print()

# Method 3: Import the whole module
from robot_package import sensors

print("Method 3: Import whole module")
print(f"  Temperature: {sensors.get_sensor_reading('temperature')}")
print()

print("=" * 50)
print("Success! Your package imports are working.")
print("=" * 50)

