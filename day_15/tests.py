"""
🧪 Tests for Debug the Broken Robot Script

These tests will FAIL until you fix all the bugs in project.py!

Usage:
    python tests.py

Your goal: Make all tests pass by fixing the bugs.
"""

import math
from project import (
    BuggyRobot,
    calculate_path_length,
    count_turns,
    find_furthest_position,
)


# ============================================================
# ROBOT INITIALIZATION TESTS
# ============================================================

def test_init_position_history():
    """Test: Position history should be a list"""
    robot = BuggyRobot("Test")
    assert isinstance(robot.position_history, list), \
        f"❌ BUG 1: position_history should be a list, got {type(robot.position_history)}"
    assert (0, 0) in robot.position_history, \
        f"❌ BUG 1: position_history should contain starting position"
    print("✅ Test 1 passed: Position history is a list")


# ============================================================
# MOVEMENT TESTS
# ============================================================

def test_move_east():
    """Test: Move east (heading 0)"""
    robot = BuggyRobot("Test")
    robot.heading = 0
    robot.position_history = [(0, 0)]  # Reset for this test
    robot.move(10)
    pos = robot.get_position()
    assert abs(pos[0] - 10) < 0.1, f"❌ BUG 2/3: x should be ~10, got {pos[0]}"
    assert abs(pos[1] - 0) < 0.1, f"❌ BUG 2/3: y should be ~0, got {pos[1]}"
    print("✅ Test 2 passed: Move east works")


def test_move_north():
    """Test: Move north (heading 90)"""
    robot = BuggyRobot("Test")
    robot.heading = 90
    robot.position_history = [(0, 0)]
    robot.move(10)
    pos = robot.get_position()
    assert abs(pos[0] - 0) < 0.1, f"❌ BUG 2/3: x should be ~0, got {pos[0]}"
    assert abs(pos[1] - 10) < 0.1, f"❌ BUG 2/3: y should be ~10, got {pos[1]}"
    print("✅ Test 3 passed: Move north works")


def test_total_distance_increases():
    """Test: Total distance should increase"""
    robot = BuggyRobot("Test")
    robot.position_history = [(0, 0)]
    robot.move(10)
    assert robot.total_distance == 10, \
        f"❌ BUG 4: total_distance should be 10, got {robot.total_distance}"
    print("✅ Test 4 passed: Total distance increases")


def test_position_history_updates():
    """Test: Position history should append"""
    robot = BuggyRobot("Test")
    robot.position_history = [(0, 0)]
    robot.move(10)
    assert len(robot.position_history) == 2, \
        f"❌ BUG 5: history should have 2 entries, got {len(robot.position_history)}"
    print("✅ Test 5 passed: Position history updates")


# ============================================================
# TURN TESTS
# ============================================================

def test_turn_left():
    """Test: Turn left increases heading"""
    robot = BuggyRobot("Test")
    robot.heading = 0
    robot.turn(90)
    assert robot.heading == 90, \
        f"❌ BUG 6: heading should be 90, got {robot.heading}"
    print("✅ Test 6 passed: Turn left works")


def test_turn_wraparound():
    """Test: Heading wraps at 360"""
    robot = BuggyRobot("Test")
    robot.heading = 350
    robot.turn(20)
    assert robot.heading == 10, \
        f"❌ BUG 7: heading should be 10 (370 % 360), got {robot.heading}"
    print("✅ Test 7 passed: Turn wraparound works")


# ============================================================
# POSITION TESTS
# ============================================================

def test_get_position_rounds_both():
    """Test: Both x and y should be rounded"""
    robot = BuggyRobot("Test")
    robot.x = 1.23456
    robot.y = 7.89012
    pos = robot.get_position()
    assert pos[1] == 7.89, \
        f"❌ BUG 8: y should be rounded to 7.89, got {pos[1]}"
    print("✅ Test 8 passed: Both coordinates rounded")


# ============================================================
# DISTANCE FROM ORIGIN TESTS
# ============================================================

def test_distance_from_origin():
    """Test: Distance calculation uses squares"""
    robot = BuggyRobot("Test")
    robot.x = 3
    robot.y = 4
    dist = robot.get_distance_from_origin()
    assert abs(dist - 5) < 0.01, \
        f"❌ BUG 9: distance should be 5 (3-4-5 triangle), got {dist}"
    print("✅ Test 9 passed: Distance from origin correct")


# ============================================================
# STATUS TESTS
# ============================================================

def test_status_includes_name():
    """Test: Status includes robot name"""
    robot = BuggyRobot("TestBot")
    status = robot.get_status()
    assert "TestBot" in status, \
        f"❌ BUG 10: status should include 'TestBot', got '{status}'"
    print("✅ Test 10 passed: Status includes name")


# ============================================================
# PATH LENGTH TESTS
# ============================================================

def test_path_length():
    """Test: Calculate path length correctly"""
    positions = [(0, 0), (3, 0), (3, 4)]
    # Path: 0->3 on x (3 units), then 0->4 on y (4 units) = 7 total
    length = calculate_path_length(positions)
    assert abs(length - 7) < 0.01, \
        f"❌ BUG 11: path length should be 7, got {length}"
    print("✅ Test 11 passed: Path length correct")


# ============================================================
# COUNT TURNS TESTS
# ============================================================

def test_count_turns():
    """Test: Count turn commands"""
    commands = ["F10", "L90", "F5", "R45", "F3"]
    count = count_turns(commands)
    assert count == 2, \
        f"❌ BUG 12: should count 2 turns (L90, R45), got {count}"
    print("✅ Test 12 passed: Turn count correct")


# ============================================================
# FURTHEST POSITION TESTS
# ============================================================

def test_furthest_position():
    """Test: Find furthest position from origin"""
    positions = [(1, 0), (5, 0), (3, 0)]
    furthest = find_furthest_position(positions)
    assert furthest == (5, 0), \
        f"❌ BUG 13/14: furthest should be (5, 0), got {furthest}"
    print("✅ Test 13 passed: Furthest position correct")


def test_furthest_with_negatives():
    """Test: Furthest works with negative coordinates"""
    positions = [(1, 1), (-10, 0), (2, 2)]
    furthest = find_furthest_position(positions)
    # (-10, 0) is furthest: distance = 10
    # (2, 2) distance = 2.83
    assert furthest == (-10, 0), \
        f"❌ BUG 14: furthest should be (-10, 0), got {furthest}"
    print("✅ Test 14 passed: Furthest with negatives correct")


def run_all_tests():
    """Run all tests and show results."""
    print("=" * 50)
    print("🐛 Running Bug Hunt Tests")
    print("=" * 50)
    print()
    print("Find and fix all bugs in project.py to pass these tests!")
    print()
    
    tests = [
        test_init_position_history,
        test_move_east,
        test_move_north,
        test_total_distance_increases,
        test_position_history_updates,
        test_turn_left,
        test_turn_wraparound,
        test_get_position_rounds_both,
        test_distance_from_origin,
        test_status_includes_name,
        test_path_length,
        test_count_turns,
        test_furthest_position,
        test_furthest_with_negatives,
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
        except Exception as e:
            print(f"❌ {test.__name__} crashed: {e}")
            failed += 1
    
    print()
    print("=" * 50)
    print(f"Results: {passed} passed, {failed} failed")
    print(f"Bugs remaining: {failed}")
    if failed == 0:
        print("🎉 All bugs fixed! Great debugging!")
    else:
        print("🔍 Keep hunting those bugs!")
    print("=" * 50)


if __name__ == "__main__":
    run_all_tests()

