"""
🧪 Tests for Robot Class

Run this file to check if your Robot class is correct!

Usage:
    python tests.py

These tests automatically import your Robot class from project.py
and verify that your implementation is correct.
"""

from project import Robot


# ============================================================
# INITIALIZATION TESTS
# ============================================================

def test_init_name():
    """Test: Robot stores name correctly"""
    robot = Robot("Scout")
    assert robot.name == "Scout", f"❌ Expected name 'Scout', got '{robot.name}'"
    print("✅ Test 1 passed: Robot stores name correctly")


def test_init_default_battery():
    """Test: Default battery is 100"""
    robot = Robot("Scout")
    assert robot.battery == 100, f"❌ Expected battery 100, got {robot.battery}"
    print("✅ Test 2 passed: Default battery is 100")


def test_init_custom_battery():
    """Test: Custom battery value works"""
    robot = Robot("Scout", battery=50)
    assert robot.battery == 50, f"❌ Expected battery 50, got {robot.battery}"
    print("✅ Test 3 passed: Custom battery value works")


def test_init_default_position():
    """Test: Default position is (0, 0)"""
    robot = Robot("Scout")
    assert robot.position == (0, 0), f"❌ Expected position (0, 0), got {robot.position}"
    print("✅ Test 4 passed: Default position is (0, 0)")


def test_init_custom_position():
    """Test: Custom position works"""
    robot = Robot("Scout", position=(5, 10))
    assert robot.position == (5, 10), f"❌ Expected position (5, 10), got {robot.position}"
    print("✅ Test 5 passed: Custom position works")


def test_init_heading():
    """Test: Initial heading is 0"""
    robot = Robot("Scout")
    assert robot.heading == 0, f"❌ Expected heading 0, got {robot.heading}"
    print("✅ Test 6 passed: Initial heading is 0")


# ============================================================
# CONSUME BATTERY TESTS
# ============================================================

def test_consume_battery_basic():
    """Test: Consumes battery correctly"""
    robot = Robot("Scout", battery=100)
    robot.consume_battery(30)
    assert robot.battery == 70, f"❌ Expected battery 70, got {robot.battery}"
    print("✅ Test 7 passed: Consumes battery correctly")


def test_consume_battery_no_negative():
    """Test: Battery doesn't go below 0"""
    robot = Robot("Scout", battery=20)
    robot.consume_battery(50)
    assert robot.battery == 0, f"❌ Expected battery 0 (not negative), got {robot.battery}"
    print("✅ Test 8 passed: Battery doesn't go below 0")


def test_consume_battery_exact():
    """Test: Consuming exact amount works"""
    robot = Robot("Scout", battery=30)
    robot.consume_battery(30)
    assert robot.battery == 0, f"❌ Expected battery 0, got {robot.battery}"
    print("✅ Test 9 passed: Consuming exact battery amount works")


# ============================================================
# CHARGE TESTS
# ============================================================

def test_charge_basic():
    """Test: Charges battery correctly"""
    robot = Robot("Scout", battery=50)
    robot.charge(30)
    assert robot.battery == 80, f"❌ Expected battery 80, got {robot.battery}"
    print("✅ Test 10 passed: Charges battery correctly")


def test_charge_no_exceed_100():
    """Test: Battery doesn't exceed 100"""
    robot = Robot("Scout", battery=80)
    robot.charge(50)
    assert robot.battery == 100, f"❌ Expected battery 100 (not 130), got {robot.battery}"
    print("✅ Test 11 passed: Battery doesn't exceed 100")


def test_charge_from_empty():
    """Test: Can charge from 0"""
    robot = Robot("Scout", battery=0)
    robot.charge(25)
    assert robot.battery == 25, f"❌ Expected battery 25, got {robot.battery}"
    print("✅ Test 12 passed: Can charge from empty")


# ============================================================
# MOVE TESTS
# ============================================================

def test_move_right():
    """Test: Moving right (heading 0)"""
    robot = Robot("Scout")
    robot.heading = 0
    robot.move(10)
    assert robot.position == (10, 0), f"❌ Expected (10, 0), got {robot.position}"
    print("✅ Test 13 passed: Moving right works")


def test_move_up():
    """Test: Moving up (heading 90)"""
    robot = Robot("Scout")
    robot.heading = 90
    robot.move(10)
    assert robot.position == (0, 10), f"❌ Expected (0, 10), got {robot.position}"
    print("✅ Test 14 passed: Moving up works")


def test_move_left():
    """Test: Moving left (heading 180)"""
    robot = Robot("Scout")
    robot.heading = 180
    robot.move(10)
    assert robot.position == (-10, 0), f"❌ Expected (-10, 0), got {robot.position}"
    print("✅ Test 15 passed: Moving left works")


def test_move_down():
    """Test: Moving down (heading 270)"""
    robot = Robot("Scout")
    robot.heading = 270
    robot.move(10)
    assert robot.position == (0, -10), f"❌ Expected (0, -10), got {robot.position}"
    print("✅ Test 16 passed: Moving down works")


def test_move_consumes_battery():
    """Test: Moving consumes battery"""
    robot = Robot("Scout", battery=100)
    robot.move(25)
    assert robot.battery == 75, f"❌ Expected battery 75, got {robot.battery}"
    print("✅ Test 17 passed: Moving consumes battery")


def test_move_no_battery():
    """Test: Can't move with no battery"""
    robot = Robot("Scout", battery=0)
    robot.move(10)
    assert robot.position == (0, 0), f"❌ Robot shouldn't move with 0 battery"
    print("✅ Test 18 passed: Can't move with no battery")


# ============================================================
# ROTATE TESTS
# ============================================================

def test_rotate_basic():
    """Test: Basic rotation"""
    robot = Robot("Scout")
    robot.rotate(90)
    assert robot.heading == 90, f"❌ Expected heading 90, got {robot.heading}"
    print("✅ Test 19 passed: Basic rotation works")


def test_rotate_multiple():
    """Test: Multiple rotations"""
    robot = Robot("Scout")
    robot.rotate(90)
    robot.rotate(90)
    assert robot.heading == 180, f"❌ Expected heading 180, got {robot.heading}"
    print("✅ Test 20 passed: Multiple rotations work")


def test_rotate_wrap_around():
    """Test: Rotation wraps around 360"""
    robot = Robot("Scout")
    robot.heading = 270
    robot.rotate(180)
    assert robot.heading == 90, f"❌ Expected heading 90 (270+180=450, 450%360=90), got {robot.heading}"
    print("✅ Test 21 passed: Rotation wraps around correctly")


def test_rotate_negative():
    """Test: Negative rotation works"""
    robot = Robot("Scout")
    robot.heading = 90
    robot.rotate(-90)
    assert robot.heading == 0, f"❌ Expected heading 0, got {robot.heading}"
    print("✅ Test 22 passed: Negative rotation works")


def test_rotate_consumes_battery():
    """Test: Rotation consumes battery"""
    robot = Robot("Scout", battery=100)
    robot.rotate(90)
    # 1 battery per 90 degrees
    assert robot.battery == 99, f"❌ Expected battery 99, got {robot.battery}"
    print("✅ Test 23 passed: Rotation consumes battery")


def test_rotate_no_battery():
    """Test: Can't rotate with no battery"""
    robot = Robot("Scout", battery=0)
    robot.rotate(90)
    assert robot.heading == 0, f"❌ Robot shouldn't rotate with 0 battery"
    print("✅ Test 24 passed: Can't rotate with no battery")


# ============================================================
# REPORT STATUS TESTS
# ============================================================

def test_report_status_has_name():
    """Test: Status includes robot name"""
    robot = Robot("Scout")
    status = robot.report_status()
    assert "Scout" in status, f"❌ Status should include name 'Scout': {status}"
    print("✅ Test 25 passed: Status includes name")


def test_report_status_has_battery():
    """Test: Status includes battery level"""
    robot = Robot("Scout", battery=75)
    status = robot.report_status()
    assert "75" in status, f"❌ Status should include battery '75': {status}"
    print("✅ Test 26 passed: Status includes battery")


def test_report_status_has_position():
    """Test: Status includes position"""
    robot = Robot("Scout", position=(5, 10))
    status = robot.report_status()
    assert "5" in status and "10" in status, f"❌ Status should include position: {status}"
    print("✅ Test 27 passed: Status includes position")


def test_report_status_has_heading():
    """Test: Status includes heading"""
    robot = Robot("Scout")
    robot.heading = 90
    status = robot.report_status()
    assert "90" in status, f"❌ Status should include heading '90': {status}"
    print("✅ Test 28 passed: Status includes heading")


# ============================================================
# IS_OPERATIONAL PROPERTY TESTS
# ============================================================

def test_is_operational_true():
    """Test: is_operational True with battery"""
    robot = Robot("Scout", battery=50)
    assert robot.is_operational == True, f"❌ Should be operational with battery"
    print("✅ Test 29 passed: is_operational True with battery")


def test_is_operational_false():
    """Test: is_operational False with no battery"""
    robot = Robot("Scout", battery=0)
    assert robot.is_operational == False, f"❌ Should not be operational with 0 battery"
    print("✅ Test 30 passed: is_operational False with no battery")


def test_is_operational_property():
    """Test: is_operational is a property (no parentheses)"""
    robot = Robot("Scout")
    # This tests that it's a property, not a method
    result = robot.is_operational
    assert isinstance(result, bool), f"❌ is_operational should return bool, got {type(result)}"
    print("✅ Test 31 passed: is_operational is a property")


# ============================================================
# INTEGRATION TESTS
# ============================================================

def test_multiple_robots():
    """Test: Multiple robots are independent"""
    robot1 = Robot("Scout", battery=100)
    robot2 = Robot("Guard", battery=50)
    robot1.consume_battery(30)
    assert robot1.battery == 70, f"❌ Robot1 should have 70 battery"
    assert robot2.battery == 50, f"❌ Robot2 should still have 50 battery"
    print("✅ Test 32 passed: Multiple robots are independent")


def test_full_mission():
    """Test: Complete mission sequence"""
    robot = Robot("Scout")
    robot.move(20)      # battery: 100->80, position: (20,0)
    robot.rotate(90)    # battery: 80->79, heading: 90
    robot.move(10)      # battery: 79->69, position: (20,10)
    assert robot.position == (20, 10), f"❌ Expected position (20, 10)"
    assert robot.heading == 90, f"❌ Expected heading 90"
    assert robot.battery == 69, f"❌ Expected battery 69"
    print("✅ Test 33 passed: Complete mission sequence works")


def run_all_tests():
    """Run all tests and show results."""
    print("=" * 50)
    print("🤖 Running Robot Class Tests")
    print("=" * 50)
    print()
    
    tests = [
        test_init_name,
        test_init_default_battery,
        test_init_custom_battery,
        test_init_default_position,
        test_init_custom_position,
        test_init_heading,
        test_consume_battery_basic,
        test_consume_battery_no_negative,
        test_consume_battery_exact,
        test_charge_basic,
        test_charge_no_exceed_100,
        test_charge_from_empty,
        test_move_right,
        test_move_up,
        test_move_left,
        test_move_down,
        test_move_consumes_battery,
        test_move_no_battery,
        test_rotate_basic,
        test_rotate_multiple,
        test_rotate_wrap_around,
        test_rotate_negative,
        test_rotate_consumes_battery,
        test_rotate_no_battery,
        test_report_status_has_name,
        test_report_status_has_battery,
        test_report_status_has_position,
        test_report_status_has_heading,
        test_is_operational_true,
        test_is_operational_false,
        test_is_operational_property,
        test_multiple_robots,
        test_full_mission,
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
            print(f"❌ {test.__doc__.split(':')[0]}: Method not implemented yet")
            failed += 1
        except AttributeError as e:
            print(f"❌ {test.__doc__.split(':')[0]}: Attribute missing - {e}")
            failed += 1
        except Exception as e:
            print(f"❌ {test.__name__} crashed: {e}")
            failed += 1
    
    print()
    print("=" * 50)
    print(f"Results: {passed} passed, {failed} failed")
    if failed == 0:
        print("🎉 All tests passed! Your Robot class is fully operational!")
    else:
        print("💪 Keep coding, your robot needs its methods!")
    print("=" * 50)


if __name__ == "__main__":
    run_all_tests()

