"""
🧪 Tests for Robot Inventory & Config Manager

Run this file to check if your config manager is correct!

Usage:
    python tests.py

These tests automatically import your functions from project.py
and verify that your implementation is correct.
"""

from project import (
    create_robot_config,
    get_total_power_draw,
    add_sensor,
    find_robot_by_name,
    get_fleet_summary,
    get_most_capable_robot,
)


# ============================================================
# CREATE ROBOT CONFIG TESTS
# ============================================================

def test_create_config_returns_dict():
    """Test: Returns a dictionary"""
    result = create_robot_config("Scout", 4, 3, 100)
    assert isinstance(result, dict), f"❌ Expected dict, got {type(result)}"
    print("✅ Test 1 passed: Returns a dictionary")


def test_create_config_has_name():
    """Test: Config contains correct name"""
    result = create_robot_config("Scout", 4, 3, 100)
    assert result["name"] == "Scout", f"❌ Expected name 'Scout', got '{result.get('name')}'"
    print("✅ Test 2 passed: Config has correct name")


def test_create_config_has_motors():
    """Test: Config contains motors dict"""
    result = create_robot_config("Scout", 4, 3, 100)
    assert "motors" in result, f"❌ Missing 'motors' key"
    assert result["motors"]["count"] == 4, f"❌ Expected motor count 4, got {result['motors'].get('count')}"
    assert result["motors"]["power_per_motor"] == 25, f"❌ Expected power_per_motor 25"
    print("✅ Test 3 passed: Config has motors with count and power")


def test_create_config_has_battery():
    """Test: Config contains battery capacity"""
    result = create_robot_config("Scout", 4, 3, 100)
    assert result["battery_wh"] == 100, f"❌ Expected battery_wh 100, got {result.get('battery_wh')}"
    print("✅ Test 4 passed: Config has correct battery capacity")


def test_create_config_has_sensor_count():
    """Test: Config contains sensor count"""
    result = create_robot_config("Scout", 4, 3, 100)
    assert result["sensor_count"] == 3, f"❌ Expected sensor_count 3, got {result.get('sensor_count')}"
    print("✅ Test 5 passed: Config has correct sensor count")


# ============================================================
# GET TOTAL POWER DRAW TESTS
# ============================================================

def test_power_draw_basic():
    """Test: Basic power calculation"""
    robot = {"motors": {"count": 4, "power_per_motor": 25}}
    result = get_total_power_draw(robot)
    assert result == 100, f"❌ Expected 100W (4×25), got {result}"
    print("✅ Test 6 passed: Basic power draw (4×25 = 100W)")


def test_power_draw_different_values():
    """Test: Different motor configuration"""
    robot = {"motors": {"count": 6, "power_per_motor": 25}}
    result = get_total_power_draw(robot)
    assert result == 150, f"❌ Expected 150W (6×25), got {result}"
    print("✅ Test 7 passed: Different motor count (6×25 = 150W)")


def test_power_draw_zero_motors():
    """Test: Zero motors = zero power"""
    robot = {"motors": {"count": 0, "power_per_motor": 25}}
    result = get_total_power_draw(robot)
    assert result == 0, f"❌ Expected 0W, got {result}"
    print("✅ Test 8 passed: Zero motors = zero power")


# ============================================================
# ADD SENSOR TESTS
# ============================================================

def test_add_sensor_creates_entry():
    """Test: Adds sensor to dictionary"""
    robot = {"sensors": {}}
    result = add_sensor(robot, "lidar", 10.0)
    assert "lidar" in result["sensors"], f"❌ Sensor 'lidar' not added"
    assert result["sensors"]["lidar"] == 10.0, f"❌ Expected range 10.0"
    print("✅ Test 9 passed: Sensor added to dictionary")


def test_add_sensor_multiple():
    """Test: Can add multiple sensors"""
    robot = {"sensors": {}}
    add_sensor(robot, "lidar", 10.0)
    add_sensor(robot, "camera", 5.0)
    result = add_sensor(robot, "ultrasonic", 3.0)
    assert len(result["sensors"]) == 3, f"❌ Expected 3 sensors"
    print("✅ Test 10 passed: Multiple sensors added")


def test_add_sensor_returns_robot():
    """Test: Returns the robot dictionary"""
    robot = {"name": "Scout", "sensors": {}}
    result = add_sensor(robot, "lidar", 10.0)
    assert result["name"] == "Scout", f"❌ Should return the robot dict"
    print("✅ Test 11 passed: Returns robot dictionary")


# ============================================================
# FIND ROBOT BY NAME TESTS
# ============================================================

def test_find_robot_exists():
    """Test: Finds existing robot"""
    fleet = [
        {"name": "Scout", "battery_wh": 100},
        {"name": "Guard", "battery_wh": 150}
    ]
    result = find_robot_by_name(fleet, "Scout")
    assert result is not None, f"❌ Should find Scout"
    assert result["name"] == "Scout", f"❌ Wrong robot returned"
    print("✅ Test 12 passed: Finds existing robot")


def test_find_robot_not_exists():
    """Test: Returns None for missing robot"""
    fleet = [{"name": "Scout"}, {"name": "Guard"}]
    result = find_robot_by_name(fleet, "Unknown")
    assert result is None, f"❌ Should return None for missing robot"
    print("✅ Test 13 passed: Returns None for missing robot")


def test_find_robot_empty_fleet():
    """Test: Returns None for empty fleet"""
    fleet = []
    result = find_robot_by_name(fleet, "Scout")
    assert result is None, f"❌ Should return None for empty fleet"
    print("✅ Test 14 passed: Returns None for empty fleet")


def test_find_robot_returns_full_dict():
    """Test: Returns full robot dictionary"""
    fleet = [{"name": "Scout", "battery_wh": 100, "sensor_count": 3}]
    result = find_robot_by_name(fleet, "Scout")
    assert result["battery_wh"] == 100, f"❌ Should return full robot dict"
    assert result["sensor_count"] == 3, f"❌ Should include all keys"
    print("✅ Test 15 passed: Returns full robot dictionary")


# ============================================================
# GET FLEET SUMMARY TESTS
# ============================================================

def test_fleet_summary_returns_dict():
    """Test: Returns a dictionary"""
    fleet = [{"battery_wh": 100, "motors": {"count": 4}}]
    result = get_fleet_summary(fleet)
    assert isinstance(result, dict), f"❌ Expected dict, got {type(result)}"
    print("✅ Test 16 passed: Returns a dictionary")


def test_fleet_summary_total_robots():
    """Test: Counts total robots"""
    fleet = [
        {"battery_wh": 100, "motors": {"count": 4}},
        {"battery_wh": 150, "motors": {"count": 6}}
    ]
    result = get_fleet_summary(fleet)
    assert result["total_robots"] == 2, f"❌ Expected 2 robots, got {result.get('total_robots')}"
    print("✅ Test 17 passed: Counts total robots")


def test_fleet_summary_total_battery():
    """Test: Sums battery capacity"""
    fleet = [
        {"battery_wh": 100, "motors": {"count": 4}},
        {"battery_wh": 150, "motors": {"count": 6}}
    ]
    result = get_fleet_summary(fleet)
    assert result["total_battery_wh"] == 250, f"❌ Expected 250Wh, got {result.get('total_battery_wh')}"
    print("✅ Test 18 passed: Sums battery capacity")


def test_fleet_summary_total_motors():
    """Test: Sums motor counts"""
    fleet = [
        {"battery_wh": 100, "motors": {"count": 4}},
        {"battery_wh": 150, "motors": {"count": 6}}
    ]
    result = get_fleet_summary(fleet)
    assert result["total_motors"] == 10, f"❌ Expected 10 motors, got {result.get('total_motors')}"
    print("✅ Test 19 passed: Sums motor counts")


def test_fleet_summary_empty():
    """Test: Handles empty fleet"""
    fleet = []
    result = get_fleet_summary(fleet)
    assert result["total_robots"] == 0, f"❌ Expected 0 robots"
    assert result["total_battery_wh"] == 0, f"❌ Expected 0 battery"
    assert result["total_motors"] == 0, f"❌ Expected 0 motors"
    print("✅ Test 20 passed: Handles empty fleet")


# ============================================================
# GET MOST CAPABLE ROBOT TESTS
# ============================================================

def test_most_capable_finds_best():
    """Test: Finds robot with most sensors"""
    fleet = [
        {"name": "Scout", "sensor_count": 3},
        {"name": "Guard", "sensor_count": 5},
        {"name": "Worker", "sensor_count": 2}
    ]
    result = get_most_capable_robot(fleet)
    assert result == "Guard", f"❌ Expected 'Guard' (5 sensors), got '{result}'"
    print("✅ Test 21 passed: Finds robot with most sensors")


def test_most_capable_single_robot():
    """Test: Works with single robot"""
    fleet = [{"name": "Solo", "sensor_count": 4}]
    result = get_most_capable_robot(fleet)
    assert result == "Solo", f"❌ Expected 'Solo', got '{result}'"
    print("✅ Test 22 passed: Works with single robot")


def test_most_capable_empty_fleet():
    """Test: Returns None for empty fleet"""
    fleet = []
    result = get_most_capable_robot(fleet)
    assert result is None, f"❌ Expected None for empty fleet, got '{result}'"
    print("✅ Test 23 passed: Returns None for empty fleet")


def test_most_capable_first_wins_tie():
    """Test: Handles tie by returning first found"""
    fleet = [
        {"name": "Alpha", "sensor_count": 5},
        {"name": "Beta", "sensor_count": 5}
    ]
    result = get_most_capable_robot(fleet)
    assert result in ["Alpha", "Beta"], f"❌ Expected 'Alpha' or 'Beta', got '{result}'"
    print("✅ Test 24 passed: Handles ties")


def run_all_tests():
    """Run all tests and show results."""
    print("=" * 50)
    print("🤖 Running Robot Inventory & Config Manager Tests")
    print("=" * 50)
    print()
    
    tests = [
        test_create_config_returns_dict,
        test_create_config_has_name,
        test_create_config_has_motors,
        test_create_config_has_battery,
        test_create_config_has_sensor_count,
        test_power_draw_basic,
        test_power_draw_different_values,
        test_power_draw_zero_motors,
        test_add_sensor_creates_entry,
        test_add_sensor_multiple,
        test_add_sensor_returns_robot,
        test_find_robot_exists,
        test_find_robot_not_exists,
        test_find_robot_empty_fleet,
        test_find_robot_returns_full_dict,
        test_fleet_summary_returns_dict,
        test_fleet_summary_total_robots,
        test_fleet_summary_total_battery,
        test_fleet_summary_total_motors,
        test_fleet_summary_empty,
        test_most_capable_finds_best,
        test_most_capable_single_robot,
        test_most_capable_empty_fleet,
        test_most_capable_first_wins_tie,
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
            print(f"❌ {test.__doc__.split(':')[0]}: Function not implemented yet (returned None)")
            failed += 1
        except Exception as e:
            print(f"❌ {test.__name__} crashed: {e}")
            failed += 1
    
    print()
    print("=" * 50)
    print(f"Results: {passed} passed, {failed} failed")
    if failed == 0:
        print("🎉 All tests passed! Robot fleet ready for deployment!")
    else:
        print("💪 Keep configuring, your robots need you!")
    print("=" * 50)


if __name__ == "__main__":
    run_all_tests()

