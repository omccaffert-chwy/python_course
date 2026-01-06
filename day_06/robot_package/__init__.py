# This file marks robot_package as a Python package
# It can be empty, or you can use it to expose specific items

# Example: expose commonly used items at the package level
from .sensors import get_sensor_reading
from .motors import move_forward

# Now users can do:
#   from robot_package import get_sensor_reading
# Instead of:
#   from robot_package.sensors import get_sensor_reading

print("robot_package initialized!")  # This runs when the package is imported

