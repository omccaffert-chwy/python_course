"""
🤖 Robot Class - Sensors & Actions

This project teaches:
- Object-Oriented Programming (OOP) basics
- Creating classes with __init__
- Instance attributes (self.name, self.battery, etc.)
- Instance methods (self as first parameter)
- Properties (@property decorator)

Your Task:
----------
Complete the Robot class below with these features:

Attributes:
- name: Robot's name (string)
- battery: Current battery level 0-100 (integer)
- position: Current (x, y) coordinates (tuple)
- heading: Current direction in degrees 0-359 (integer)

Methods:
- move(distance): Move forward and consume battery
- rotate(degrees): Turn and consume battery
- consume_battery(amount): Reduce battery level
- charge(amount): Recharge battery
- report_status(): Return a status string

Property:
- is_operational: True if battery > 0

Example Usage:
--------------
robot = Robot("Scout")
print(robot.name)           # "Scout"
print(robot.battery)        # 100
print(robot.position)       # (0, 0)

robot.move(10)
print(robot.position)       # (10, 0) - moved 10 units forward
print(robot.battery)        # 90 - consumed 10% battery

robot.rotate(90)
print(robot.heading)        # 90 degrees
"""


from math import dist
from operator import is_
from os import name
from turtle import position


class Robot:
    """
    A class representing a robot with battery, position, and movement.
    """
    
    def __init__(self, name, battery=100, position=(0, 0)):
        """
        Initialize a new Robot instance.
        
        Args:
            name: The robot's name (string)
            battery: Starting battery level, default 100 (integer 0-100)
            position: Starting (x, y) position, default (0, 0) (tuple)
        
        Should set these instance attributes:
            self.name = name
            self.battery = battery
            self.position = position
            self.heading = 0  (starting direction in degrees)
        
        Example:
            robot = Robot("Scout")
            robot.name -> "Scout"
            robot.battery -> 100
            robot.position -> (0, 0)
            robot.heading -> 0
        """
        # TODO: Set self.name to the name parameter
        # TODO: Set self.battery to the battery parameter
        # TODO: Set self.position to the position parameter
        # TODO: Set self.heading to 0 (facing right/east)
        self.name = name
        self.battery = battery
        self.position =  position
        self.heading = 0
        pass
    
    def consume_battery(self, amount):
        """
        Reduce the robot's battery level.
        
        Args:
            amount: How much battery to consume (integer)
        
        Rules:
            - Subtract amount from self.battery
            - Battery cannot go below 0
        
        Example:
            robot.battery = 50
            robot.consume_battery(30)
            robot.battery -> 20
            
            robot.consume_battery(30)
            robot.battery -> 0 (not -10!)
        """
        # TODO: Reduce battery by amount, but don't go below 0
        if self.battery >= amount:
            self.battery = self.battery - amount
        else:
            self.battery = 0
        pass
    
    def charge(self, amount):
        """
        Recharge the robot's battery.
        
        Args:
            amount: How much battery to add (integer)
        
        Rules:
            - Add amount to self.battery
            - Battery cannot exceed 100
        
        Example:
            robot.battery = 50
            robot.charge(30)
            robot.battery -> 80
            
            robot.charge(50)
            robot.battery -> 100 (not 130!)
        """
        # TODO: Increase battery by amount, but don't exceed 100
        self.charge = amount
        self.battery = self.battery + self.charge
        if self.battery > 100:
            self.battery = 100
        pass
    
    def move(self, distance):
        """
        Move the robot forward in its current heading direction.
        
        Args:
            distance: How far to move (integer)
        
        Rules:
            - Update position based on heading:
                - heading 0: move in +x direction (right)
                - heading 90: move in +y direction (up)
                - heading 180: move in -x direction (left)
                - heading 270: move in -y direction (down)
            - Consume battery equal to distance moved
            - Only move if robot is_operational
        
        Example:
            robot.position = (0, 0)
            robot.heading = 0
            robot.move(10)
            robot.position -> (10, 0)
            robot.battery -> 90 (was 100, consumed 10)
        
        Hint: For simplicity, only handle 0, 90, 180, 270 degree headings
        """
        # TODO: Check if robot is_operational first
        # TODO: Update position based on heading
        # TODO: Consume battery equal to distance
        new_position_list = list(self.position)
        if self.is_operational:
            self.consume_battery(distance)
            if self.heading == 0:
                new_position_list[0] = new_position_list[0] + distance
                self.position = tuple(new_position_list)
            if self.heading == 90:
                new_position_list[1] = new_position_list[1] + distance
                self.position = tuple(new_position_list)
            if self.heading == 180:
                new_position_list[0] = new_position_list[0] - distance
                self.position = tuple(new_position_list)
            if self.heading == 270:
                new_position_list[1] = new_position_list[1] - distance
                self.position = tuple(new_position_list)
        pass
    
    def rotate(self, degrees):
        """
        Rotate the robot by the given degrees.
        
        Args:
            degrees: How many degrees to turn (can be negative)
        
        Rules:
            - Add degrees to self.heading
            - Keep heading in range 0-359 (use modulo %)
            - Consume 1 battery per 90 degrees of rotation
            - Only rotate if robot is_operational
        
        Example:
            robot.heading = 0
            robot.rotate(90)
            robot.heading -> 90
            
            robot.rotate(180)
            robot.heading -> 270
            
            robot.rotate(180)
            robot.heading -> 90 (wraps around: 270+180=450, 450%360=90)
        """
        # TODO: Check if robot is_operational first
        # TODO: Update heading (remember to use % 360 to wrap)
        # TODO: Consume battery (1 per 90 degrees, use abs() for negative)
        if self.is_operational:
            self.heading = self.heading + degrees
            if self.heading > 360:
                self.heading = self.heading%360
        self.consume_battery(abs(degrees)/90)
        pass
    
    def report_status(self):
        """
        Return a string describing the robot's current status.
        
        Returns:
            A formatted string with robot info:
            "Robot {name}: Battery {battery}%, Position {position}, Heading {heading}°"
        
        Example:
            robot = Robot("Scout")
            robot.report_status() -> 
            "Robot Scout: Battery 100%, Position (0, 0), Heading 0°"
        """
        # TODO: Return a formatted status string
        report = (f"Robot {self.name}: Battery {self.battery}%, Position {self.position}, Heading {self.heading}°")
        return report
        pass
    
    @property
    def is_operational(self):
        """
        Check if the robot can still operate.
        
        Returns:
            True if battery > 0, False otherwise
        
        Example:
            robot.battery = 50
            robot.is_operational -> True
            
            robot.battery = 0
            robot.is_operational -> False
        
        Note: This is a @property, so access it like robot.is_operational
              (no parentheses), not robot.is_operational()
        """
        # TODO: Return True if battery > 0, False otherwise
        if self.battery > 0:
            return True
        else:
            return False
        pass

