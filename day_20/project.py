"""
🤖 Capstone: Robot Control & Analysis Tool

This is your CAPSTONE PROJECT!

Choose ONE of two paths:

PATH A: SIMULATION
------------------
Build a robot simulator with:
- Live robot control
- Mission logging
- Replay past missions
- Visual feedback

PATH B: DATA ANALYSIS
---------------------
Build a sensor log dashboard with:
- Load CSV logs
- Compute statistics
- Filter and analyze data
- Generate reports

Your Task:
----------
Complete the functions for YOUR CHOSEN PATH.
You don't need to complete both paths!

This project combines everything you've learned:
- Classes and OOP
- File I/O
- Data structures
- Functions
- Error handling
"""

import json
import os
from datetime import datetime

# ============================================================
# PATH A: SIMULATION
# ============================================================

class SimulatedRobot:
    """A robot simulator for Path A."""
    
    def __init__(self, name):
        """Initialize the simulated robot."""
        self.name = name
        self.x = 0
        self.y = 0
        self.heading = 0
        self.battery = 100
        self.mission_log = []
        self.is_recording = False
        self.current_mission = []
    
    def start_recording(self):
        """Start recording a mission."""
        # TODO: Set is_recording to True, clear current_mission
        pass
    
    def stop_recording(self):
        """Stop recording and save the mission."""
        # TODO: Stop recording, save current_mission to mission_log
        pass
    
    def move(self, distance):
        """Move forward and record if recording."""
        # TODO: Update position, record action
        pass
    
    def turn(self, degrees):
        """Turn and record if recording."""
        # TODO: Update heading, record action
        pass
    
    def replay_mission(self, mission_index):
        """Replay a recorded mission."""
        # TODO: Execute all actions from a saved mission
        pass
    
    def get_status(self):
        """Get current robot status."""
        # TODO: Return status dictionary
        pass
    
    def save_missions(self, filename):
        """Save all missions to a file."""
        # TODO: Save mission_log to JSON file
        pass
    
    def load_missions(self, filename):
        """Load missions from a file."""
        # TODO: Load mission_log from JSON file
        pass


class SimulationController:
    """Controls the simulation for Path A."""
    
    def __init__(self):
        """Initialize the controller."""
        self.robots = {}
        self.selected_robot = None
    
    def add_robot(self, name):
        """Add a new robot to the simulation."""
        # TODO: Create and store new SimulatedRobot
        pass
    
    def select_robot(self, name):
        """Select a robot to control."""
        # TODO: Set selected_robot
        pass
    
    def execute_command(self, command):
        """
        Execute a command on the selected robot.
        
        Commands:
        - "forward 10" - move forward 10 units
        - "turn 90" - turn 90 degrees
        - "record" - start recording
        - "stop" - stop recording
        - "replay 0" - replay mission 0
        - "status" - get status
        """
        # TODO: Parse and execute command
        pass
    
    def get_simulation_summary(self):
        """Get summary of all robots and their missions."""
        # TODO: Return summary dictionary
        pass


# ============================================================
# PATH B: DATA ANALYSIS
# ============================================================

class SensorLogAnalyzer:
    """Analyzes robot sensor logs for Path B."""
    
    def __init__(self):
        """Initialize the analyzer."""
        self.data = []
        self.filename = None
    
    def load_csv(self, filename):
        """
        Load sensor data from a CSV file.
        
        Expected columns: timestamp, robot_id, distance, battery, errors
        """
        # TODO: Load CSV data into self.data
        pass
    
    def get_total_runs(self):
        """Get total number of runs in the data."""
        # TODO: Return count of data entries
        pass
    
    def get_average_distance(self):
        """Calculate average distance across all runs."""
        # TODO: Calculate and return average
        pass
    
    def get_runs_by_robot(self, robot_id):
        """Get all runs for a specific robot."""
        # TODO: Filter and return runs
        pass
    
    def get_error_runs(self):
        """Get all runs that had errors."""
        # TODO: Filter runs where errors > 0
        pass
    
    def get_low_battery_runs(self, threshold=20):
        """Get runs where battery dropped below threshold."""
        # TODO: Filter runs by battery level
        pass
    
    def calculate_statistics(self):
        """
        Calculate comprehensive statistics.
        
        Returns dict with:
        - total_runs
        - total_distance
        - average_distance
        - total_errors
        - runs_with_errors
        - average_battery_consumption
        """
        # TODO: Calculate all statistics
        pass
    
    def generate_report(self):
        """Generate a formatted text report."""
        # TODO: Create and return report string
        pass


class Dashboard:
    """A simple dashboard for Path B analysis."""
    
    def __init__(self):
        """Initialize the dashboard."""
        self.analyzer = SensorLogAnalyzer()
        self.reports = []
    
    def load_data(self, filename):
        """Load data into the analyzer."""
        # TODO: Load data and return success status
        pass
    
    def run_analysis(self):
        """Run full analysis and store report."""
        # TODO: Generate and store report
        pass
    
    def get_alerts(self):
        """
        Get any alerts based on the data.
        
        Alerts for:
        - High error rate (> 10% of runs)
        - Low average battery
        - Any robot with all failed runs
        """
        # TODO: Generate and return alerts list
        pass
    
    def save_report(self, filename):
        """Save the latest report to a file."""
        # TODO: Save report to text file
        pass


# ============================================================
# SHARED UTILITIES
# ============================================================

def create_sample_csv(filename):
    """
    Create a sample CSV file for testing Path B.
    
    Creates a file with sample sensor log data.
    """
    sample_data = """timestamp,robot_id,distance,battery,errors
2024-01-15 09:00,Scout,150.5,75,0
2024-01-15 10:30,Scout,200.2,45,1
2024-01-15 14:00,Guard,175.8,60,0
2024-01-16 09:00,Scout,120.0,80,0
2024-01-16 11:00,Guard,180.5,40,2
2024-01-16 14:00,Scout,95.3,25,0
2024-01-17 09:00,Guard,210.0,55,1
2024-01-17 11:00,Scout,165.7,70,0
"""
    with open(filename, 'w') as f:
        f.write(sample_data)
    return True


def main_menu():
    """
    Display main menu and get user choice.
    
    This can be used to create an interactive program.
    """
    menu = """
╔══════════════════════════════════════════╗
║     ROBOT CONTROL & ANALYSIS TOOL        ║
╠══════════════════════════════════════════╣
║  1. Path A: Robot Simulation             ║
║  2. Path B: Data Analysis                ║
║  3. Exit                                 ║
╚══════════════════════════════════════════╝

Select an option (1-3): """
    return menu


# ============================================================
# MAIN PROGRAM (Optional - for interactive use)
# ============================================================

if __name__ == "__main__":
    print("🤖 Welcome to the Robot Control & Analysis Tool!")
    print("This is your capstone project.")
    print()
    print("Choose your path:")
    print("  A: Build the SimulatedRobot and SimulationController classes")
    print("  B: Build the SensorLogAnalyzer and Dashboard classes")
    print()
    print("Run tests.py to check your implementation!")

