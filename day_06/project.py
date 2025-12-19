"""
🤖 Robot Energy Management Game

This project teaches:
- Combining multiple concepts (lists, loops, functions, conditionals)
- Game state management
- Random events and probability
- Functions with multiple return values
- Complex decision logic

Your Task:
----------
Complete the six functions below to build a robot mission simulator:

1. generate_task()
   - Create a random task with name, energy cost, and reward points

2. can_complete_task(battery_level, energy_cost)
   - Check if the robot has enough battery for a task

3. complete_task(battery_level, energy_cost, reward)
   - Execute a task and return new battery level and earned points

4. calculate_mission_score(completed_tasks)
   - Sum up all reward points from completed tasks

5. get_mission_status(battery_level, completed_count)
   - Return a status message based on current state

6. evaluate_mission_result(completed_tasks, battery_remaining, failed)
   - Determine final mission outcome and rating

Game Rules:
-----------
- Robot starts with 100 energy units
- Each task costs 10-40 energy and rewards 5-25 points
- Complete as many tasks as possible without running out of energy
- If you attempt a task without enough energy, MISSION FAILS
- Goal: Maximize points while managing energy wisely

Task Types (for reference):
---------------------------
- "Patrol Sector" (10-15 energy, 5-10 points)
- "Scan Environment" (15-25 energy, 10-15 points)
- "Transport Item" (20-30 energy, 12-18 points)
- "Security Check" (25-35 energy, 15-22 points)
- "Emergency Response" (30-40 energy, 20-25 points)
"""

import random


# Available task templates: (name, min_energy, max_energy, min_reward, max_reward)
TASK_TEMPLATES = [
    ("Patrol Sector", 10, 15, 5, 10),
    ("Scan Environment", 15, 25, 10, 15),
    ("Transport Item", 20, 30, 12, 18),
    ("Security Check", 25, 35, 15, 22),
    ("Emergency Response", 30, 40, 20, 25),
]


def generate_task():
    """
    Generate a random task for the robot.
    
    Randomly selects a task template and generates random
    energy cost and reward within the template's ranges.
    
    Returns:
        A dictionary with task details:
        {
            "name": task name (string),
            "energy_cost": random cost within range (integer),
            "reward": random reward within range (integer)
        }
    
    Example:
        generate_task() might return:
        {"name": "Patrol Sector", "energy_cost": 12, "reward": 7}
    
    Hint: Use random.choice() for template, random.randint() for values
    """
    # TODO: Pick a random task template
    # TODO: Generate random energy_cost and reward within the template ranges
    # TODO: Return the task dictionary
    pass


def can_complete_task(battery_level, energy_cost):
    """
    Check if the robot has enough battery to complete a task.
    
    Args:
        battery_level: Current battery level (integer)
        energy_cost: Energy required for the task (integer)
    
    Returns:
        True if battery_level >= energy_cost, False otherwise
    
    Examples:
        can_complete_task(50, 30) returns True
        can_complete_task(20, 30) returns False
        can_complete_task(30, 30) returns True (exactly enough)
    """
    # TODO: Return True if robot has enough energy, False otherwise
    pass


def complete_task(battery_level, energy_cost, reward):
    """
    Execute a task and calculate the results.
    
    Args:
        battery_level: Current battery level (integer)
        energy_cost: Energy the task will consume (integer)
        reward: Points earned for completing the task (integer)
    
    Returns:
        A tuple of (new_battery_level, points_earned)
        new_battery_level = battery_level - energy_cost
        points_earned = reward
    
    Examples:
        complete_task(100, 25, 15) returns (75, 15)
        complete_task(50, 20, 10) returns (30, 10)
    
    Note: This function assumes the task CAN be completed.
          Use can_complete_task() to check first!
    """
    # TODO: Calculate new battery level and return tuple
    pass


def calculate_mission_score(completed_tasks):
    """
    Calculate total score from all completed tasks.
    
    Args:
        completed_tasks: A list of task dictionaries, each with a "reward" key
    
    Returns:
        The sum of all reward values (integer)
    
    Examples:
        tasks = [{"reward": 10}, {"reward": 15}, {"reward": 8}]
        calculate_mission_score(tasks) returns 33
        
        calculate_mission_score([]) returns 0
    
    Hint: Use a loop to sum up all the rewards
    """
    # TODO: Loop through completed_tasks and sum the rewards
    pass


def get_mission_status(battery_level, completed_count):
    """
    Generate a status message based on current mission state.
    
    Args:
        battery_level: Current battery level (integer)
        completed_count: Number of tasks completed (integer)
    
    Returns:
        A status string based on these rules:
        - If battery_level <= 0: "Battery depleted!"
        - If battery_level < 15: "Critical battery warning!"
        - If battery_level < 30: "Low battery warning!"
        - If completed_count == 0: "Mission started. Ready for tasks."
        - Otherwise: "Mission in progress. {completed_count} tasks done."
    
    Examples:
        get_mission_status(5, 3) returns "Critical battery warning!"
        get_mission_status(50, 0) returns "Mission started. Ready for tasks."
        get_mission_status(60, 4) returns "Mission in progress. 4 tasks done."
    """
    # TODO: Use if/elif/else to return the appropriate status message
    pass


def evaluate_mission_result(completed_tasks, battery_remaining, failed):
    """
    Evaluate the final mission outcome and assign a rating.
    
    Args:
        completed_tasks: List of completed task dictionaries
        battery_remaining: Battery level at end of mission (integer)
        failed: True if mission failed (ran out of energy mid-task)
    
    Returns:
        A dictionary with mission results:
        {
            "status": "SUCCESS" or "FAILURE",
            "tasks_completed": number of tasks,
            "total_score": sum of rewards,
            "rating": "S", "A", "B", "C", or "F" based on performance
        }
    
    Rating rules:
        - "F" if failed is True
        - "S" if total_score >= 60 and battery_remaining >= 20
        - "A" if total_score >= 45
        - "B" if total_score >= 30
        - "C" otherwise
    
    Examples:
        evaluate_mission_result([{"reward": 20}, {"reward": 25}], 30, False)
        returns {"status": "SUCCESS", "tasks_completed": 2, 
                 "total_score": 45, "rating": "A"}
    """
    # TODO: Calculate total score using calculate_mission_score()
    # TODO: Determine status ("SUCCESS" or "FAILURE")
    # TODO: Determine rating based on the rules
    # TODO: Return the result dictionary
    pass

