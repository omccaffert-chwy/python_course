"""
🧪 Tests for Robot Mission Planner

Run this file to check if your mission planner is correct!

Usage:
    python tests.py
"""

import os
import json
from project import Robot, Waypoint, Mission, MissionPlanner


TEST_FILE = "test_planner.json"


def cleanup():
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)


# ============================================================
# ROBOT TESTS
# ============================================================

def test_robot_init():
    """Test: Robot initialization"""
    robot = Robot("Scout", 100, 5)
    assert robot.name == "Scout", f"❌ Name should be Scout"
    assert robot.battery_capacity == 100, f"❌ Battery capacity should be 100"
    assert robot.current_battery == 100, f"❌ Current battery should be 100"
    print("✅ Test 1 passed: Robot init")


def test_robot_can_complete():
    """Test: Robot can complete distance check"""
    robot = Robot("Scout", 100, 5)
    assert robot.can_complete_distance(50) == True, f"❌ Should complete 50"
    assert robot.can_complete_distance(150) == False, f"❌ Can't complete 150"
    print("✅ Test 2 passed: Can complete distance")


def test_robot_travel():
    """Test: Robot travel consumes battery"""
    robot = Robot("Scout", 100, 5)
    result = robot.travel(30)
    assert result == True, f"❌ Should travel successfully"
    assert robot.current_battery == 70, f"❌ Battery should be 70"
    print("✅ Test 3 passed: Travel consumes battery")


def test_robot_recharge():
    """Test: Robot recharge"""
    robot = Robot("Scout", 100, 5)
    robot.travel(50)
    robot.recharge()
    assert robot.current_battery == 100, f"❌ Should be fully charged"
    print("✅ Test 4 passed: Recharge")


def test_robot_to_dict():
    """Test: Robot to dict"""
    robot = Robot("Scout", 100, 5)
    data = robot.to_dict()
    assert data["name"] == "Scout", f"❌ Dict should have name"
    print("✅ Test 5 passed: Robot to dict")


# ============================================================
# WAYPOINT TESTS
# ============================================================

def test_waypoint_init():
    """Test: Waypoint initialization"""
    wp = Waypoint("Lab", 10, 20, 5)
    assert wp.name == "Lab", f"❌ Name should be Lab"
    assert wp.x == 10, f"❌ X should be 10"
    assert wp.y == 20, f"❌ Y should be 20"
    print("✅ Test 6 passed: Waypoint init")


def test_waypoint_distance():
    """Test: Distance between waypoints"""
    wp1 = Waypoint("A", 0, 0)
    wp2 = Waypoint("B", 3, 4)
    dist = wp1.distance_to(wp2)
    assert dist == 5.0, f"❌ Distance should be 5 (3-4-5 triangle)"
    print("✅ Test 7 passed: Waypoint distance")


def test_waypoint_to_dict():
    """Test: Waypoint to dict"""
    wp = Waypoint("Lab", 10, 20, 5)
    data = wp.to_dict()
    assert data["name"] == "Lab", f"❌ Dict should have name"
    assert data["x"] == 10, f"❌ Dict should have x"
    print("✅ Test 8 passed: Waypoint to dict")


# ============================================================
# MISSION TESTS
# ============================================================

def test_mission_init():
    """Test: Mission initialization"""
    mission = Mission("Patrol")
    assert mission.name == "Patrol", f"❌ Name should be Patrol"
    assert len(mission.waypoints) == 0, f"❌ Should start with no waypoints"
    print("✅ Test 9 passed: Mission init")


def test_mission_add_waypoint():
    """Test: Add waypoint to mission"""
    mission = Mission("Patrol")
    wp = Waypoint("Lab", 10, 20)
    mission.add_waypoint(wp)
    assert len(mission.waypoints) == 1, f"❌ Should have 1 waypoint"
    print("✅ Test 10 passed: Add waypoint")


def test_mission_total_distance():
    """Test: Mission total distance"""
    mission = Mission("Patrol")
    mission.add_waypoint(Waypoint("A", 0, 0))
    mission.add_waypoint(Waypoint("B", 3, 0))
    mission.add_waypoint(Waypoint("C", 3, 4))
    dist = mission.get_total_distance()
    assert dist == 7.0, f"❌ Total distance should be 7 (3+4)"
    print("✅ Test 11 passed: Total distance")


def test_mission_task_time():
    """Test: Mission total task time"""
    mission = Mission("Patrol")
    mission.add_waypoint(Waypoint("A", 0, 0, 5))
    mission.add_waypoint(Waypoint("B", 3, 0, 10))
    time = mission.get_total_task_time()
    assert time == 15, f"❌ Total time should be 15 minutes"
    print("✅ Test 12 passed: Task time")


# ============================================================
# MISSION PLANNER TESTS
# ============================================================

def test_planner_init():
    """Test: Planner initialization"""
    planner = MissionPlanner()
    assert len(planner.robots) == 0, f"❌ Should start with no robots"
    assert len(planner.missions) == 0, f"❌ Should start with no missions"
    print("✅ Test 13 passed: Planner init")


def test_planner_add_robot():
    """Test: Add robot to planner"""
    planner = MissionPlanner()
    robot = Robot("Scout", 100, 5)
    planner.add_robot(robot)
    assert len(planner.robots) == 1, f"❌ Should have 1 robot"
    print("✅ Test 14 passed: Add robot")


def test_planner_get_robot():
    """Test: Get robot by name"""
    planner = MissionPlanner()
    planner.add_robot(Robot("Scout", 100, 5))
    robot = planner.get_robot_by_name("Scout")
    assert robot is not None, f"❌ Should find Scout"
    assert robot.name == "Scout", f"❌ Should be Scout"
    print("✅ Test 15 passed: Get robot")


def test_planner_can_complete():
    """Test: Check if robot can complete mission"""
    planner = MissionPlanner()
    planner.add_robot(Robot("Scout", 50, 5))
    
    mission = Mission("Short")
    mission.add_waypoint(Waypoint("A", 0, 0))
    mission.add_waypoint(Waypoint("B", 10, 0))
    planner.add_mission(mission)
    
    can, reason = planner.can_robot_complete_mission("Scout", "Short")
    assert can == True, f"❌ Should be able to complete (10 < 50)"
    print("✅ Test 16 passed: Can complete mission")


def test_planner_cannot_complete():
    """Test: Robot cannot complete long mission"""
    planner = MissionPlanner()
    planner.add_robot(Robot("Scout", 20, 5))
    
    mission = Mission("Long")
    mission.add_waypoint(Waypoint("A", 0, 0))
    mission.add_waypoint(Waypoint("B", 50, 0))
    planner.add_mission(mission)
    
    can, reason = planner.can_robot_complete_mission("Scout", "Long")
    assert can == False, f"❌ Should not complete (50 > 20)"
    print("✅ Test 17 passed: Cannot complete mission")


def test_planner_save_load():
    """Test: Save and load planner"""
    cleanup()
    
    planner = MissionPlanner()
    planner.add_robot(Robot("Scout", 100, 5))
    mission = Mission("Patrol")
    mission.add_waypoint(Waypoint("Lab", 10, 20))
    planner.add_mission(mission)
    
    planner.save_to_file(TEST_FILE)
    
    planner2 = MissionPlanner()
    planner2.load_from_file(TEST_FILE)
    
    assert len(planner2.robots) == 1, f"❌ Should load 1 robot"
    assert len(planner2.missions) == 1, f"❌ Should load 1 mission"
    
    cleanup()
    print("✅ Test 18 passed: Save and load")


def test_planner_summary():
    """Test: Planner summary"""
    planner = MissionPlanner()
    planner.add_robot(Robot("Scout", 100, 5))
    planner.add_robot(Robot("Guard", 150, 3))
    
    summary = planner.get_summary()
    assert "robots" in summary or len(summary) > 0, f"❌ Should have summary"
    print("✅ Test 19 passed: Summary")


def run_all_tests():
    """Run all tests and show results."""
    print("=" * 50)
    print("🤖 Running Mission Planner Tests")
    print("=" * 50)
    print()
    
    tests = [
        test_robot_init,
        test_robot_can_complete,
        test_robot_travel,
        test_robot_recharge,
        test_robot_to_dict,
        test_waypoint_init,
        test_waypoint_distance,
        test_waypoint_to_dict,
        test_mission_init,
        test_mission_add_waypoint,
        test_mission_total_distance,
        test_mission_task_time,
        test_planner_init,
        test_planner_add_robot,
        test_planner_get_robot,
        test_planner_can_complete,
        test_planner_cannot_complete,
        test_planner_save_load,
        test_planner_summary,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(str(e))
            failed += 1
        except TypeError as e:
            print(f"❌ {test.__doc__.split(':')[0]}: Not implemented yet")
            failed += 1
        except AttributeError as e:
            print(f"❌ {test.__doc__.split(':')[0]}: Missing attribute - {e}")
            failed += 1
        except Exception as e:
            print(f"❌ {test.__name__} crashed: {e}")
            failed += 1
    
    cleanup()
    
    print()
    print("=" * 50)
    print(f"Results: {passed} passed, {failed} failed")
    if failed == 0:
        print("🎉 All tests passed! Mission planner operational!")
    else:
        print("💪 Keep coding, plan those missions!")
    print("=" * 50)


if __name__ == "__main__":
    run_all_tests()

