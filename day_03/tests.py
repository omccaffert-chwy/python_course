"""
🧪 Tests for Robot Patrol Route Generator

Run this file to check if your route generator is correct!

Usage:
    python tests.py

These tests automatically import your functions from project.py
and verify that your implementation is correct.
"""

from project import (
    get_random_waypoint,
    shuffle_route,
    generate_patrol_route,
    calculate_total_steps,
    format_route_report,
    WAYPOINTS,
)


# ============================================================
# GET RANDOM WAYPOINT TESTS
# ============================================================

def test_random_waypoint_returns_tuple():
    """Test: Returns a valid waypoint tuple"""
    waypoints = [("Lab A", 15), ("Lab B", 28), ("Storage", 42)]
    result = get_random_waypoint(waypoints)
    assert result in waypoints, f"❌ Expected one of {waypoints}, got {result}"
    print("✅ Test 1 passed: Returns a valid waypoint from list")


def test_random_waypoint_single_item():
    """Test: Works with single item list"""
    waypoints = [("Only Option", 100)]
    result = get_random_waypoint(waypoints)
    assert result == ("Only Option", 100), f"❌ Expected ('Only Option', 100), got {result}"
    print("✅ Test 2 passed: Works with single item list")


def test_random_waypoint_uses_randomness():
    """Test: Returns different values (randomness check)"""
    waypoints = [("A", 1), ("B", 2), ("C", 3), ("D", 4), ("E", 5)]
    results = set()
    for _ in range(50):
        result = get_random_waypoint(waypoints)
        results.add(result)
    # Should get at least 2 different results in 50 tries
    assert len(results) >= 2, f"❌ Expected randomness, but got same result every time"
    print("✅ Test 3 passed: Returns random waypoints")


# ============================================================
# SHUFFLE ROUTE TESTS
# ============================================================

def test_shuffle_returns_list():
    """Test: Returns a list of same length"""
    waypoints = [("A", 1), ("B", 2), ("C", 3)]
    result = shuffle_route(waypoints)
    assert isinstance(result, list), f"❌ Expected list, got {type(result)}"
    assert len(result) == len(waypoints), f"❌ Expected length {len(waypoints)}, got {len(result)}"
    print("✅ Test 4 passed: Returns list of same length")


def test_shuffle_contains_all_waypoints():
    """Test: Contains all original waypoints"""
    waypoints = [("A", 1), ("B", 2), ("C", 3)]
    result = shuffle_route(waypoints)
    for wp in waypoints:
        assert wp in result, f"❌ Missing waypoint {wp} in shuffled result"
    print("✅ Test 5 passed: Contains all original waypoints")


def test_shuffle_does_not_modify_original():
    """Test: Does not modify the original list"""
    waypoints = [("A", 1), ("B", 2), ("C", 3)]
    original_copy = waypoints.copy()
    shuffle_route(waypoints)
    assert waypoints == original_copy, f"❌ Original list was modified!"
    print("✅ Test 6 passed: Does not modify original list")


def test_shuffle_randomizes_order():
    """Test: Actually shuffles the order"""
    waypoints = [("A", 1), ("B", 2), ("C", 3), ("D", 4), ("E", 5)]
    different_orders = 0
    for _ in range(20):
        result = shuffle_route(waypoints)
        if result != waypoints:
            different_orders += 1
    # Should get at least one different order in 20 tries
    assert different_orders >= 1, f"❌ Shuffle never changed the order"
    print("✅ Test 7 passed: Shuffles the order")


# ============================================================
# GENERATE PATROL ROUTE TESTS
# ============================================================

def test_generate_route_correct_length():
    """Test: Generates route with correct number of stops"""
    waypoints = [("A", 1), ("B", 2), ("C", 3)]
    result = generate_patrol_route(waypoints, 5)
    assert len(result) == 5, f"❌ Expected 5 stops, got {len(result)}"
    print("✅ Test 8 passed: Generates correct number of stops")


def test_generate_route_valid_waypoints():
    """Test: All stops are valid waypoints"""
    waypoints = [("A", 1), ("B", 2), ("C", 3)]
    result = generate_patrol_route(waypoints, 4)
    for stop in result:
        assert stop in waypoints, f"❌ Invalid waypoint {stop} in route"
    print("✅ Test 9 passed: All stops are valid waypoints")


def test_generate_route_zero_stops():
    """Test: Handles zero stops"""
    waypoints = [("A", 1), ("B", 2)]
    result = generate_patrol_route(waypoints, 0)
    assert result == [], f"❌ Expected empty list for 0 stops, got {result}"
    print("✅ Test 10 passed: Handles zero stops")


def test_generate_route_randomness():
    """Test: Generates random routes"""
    waypoints = [("A", 1), ("B", 2), ("C", 3)]
    routes = set()
    for _ in range(30):
        result = tuple(generate_patrol_route(waypoints, 3))
        routes.add(result)
    # Should get at least 2 different routes
    assert len(routes) >= 2, f"❌ Expected different routes, but all were the same"
    print("✅ Test 11 passed: Generates random routes")


# ============================================================
# CALCULATE TOTAL STEPS TESTS
# ============================================================

def test_calculate_steps_basic():
    """Test: Basic step calculation"""
    route = [("Lab A", 15), ("Lab B", 28), ("Storage", 42)]
    result = calculate_total_steps(route)
    assert result == 85, f"❌ Expected 85, got {result}"
    print("✅ Test 12 passed: Basic calculation (15 + 28 + 42 = 85)")


def test_calculate_steps_single_stop():
    """Test: Single stop route"""
    route = [("Entrance", 10)]
    result = calculate_total_steps(route)
    assert result == 10, f"❌ Expected 10, got {result}"
    print("✅ Test 13 passed: Single stop route")


def test_calculate_steps_empty_route():
    """Test: Empty route returns 0"""
    route = []
    result = calculate_total_steps(route)
    assert result == 0, f"❌ Expected 0 for empty route, got {result}"
    print("✅ Test 14 passed: Empty route returns 0")


def test_calculate_steps_with_zeros():
    """Test: Route with zero-step waypoints"""
    route = [("Start", 0), ("Middle", 25), ("End", 0)]
    result = calculate_total_steps(route)
    assert result == 25, f"❌ Expected 25, got {result}"
    print("✅ Test 15 passed: Handles zero-step waypoints")


# ============================================================
# FORMAT ROUTE REPORT TESTS
# ============================================================

def test_format_report_basic():
    """Test: Basic report formatting"""
    route = [("Lab A", 15), ("Lab B", 28)]
    result = format_route_report(route)
    assert "Stop 1" in result and "Lab A" in result and "15" in result, \
        f"❌ Missing Stop 1 info in report: {result}"
    assert "Stop 2" in result and "Lab B" in result and "28" in result, \
        f"❌ Missing Stop 2 info in report: {result}"
    print("✅ Test 16 passed: Basic report formatting")


def test_format_report_single_stop():
    """Test: Single stop report"""
    route = [("Entrance", 10)]
    result = format_route_report(route)
    assert "Stop 1" in result and "Entrance" in result and "10" in result, \
        f"❌ Expected Stop 1 with Entrance, got: {result}"
    print("✅ Test 17 passed: Single stop report")


def test_format_report_empty_route():
    """Test: Empty route returns empty string"""
    route = []
    result = format_route_report(route)
    assert result == "" or result is None or len(result.strip()) == 0, \
        f"❌ Expected empty string for empty route, got: '{result}'"
    print("✅ Test 18 passed: Empty route returns empty/no report")


def test_format_report_contains_steps_label():
    """Test: Report contains 'steps' label"""
    route = [("Lab A", 15)]
    result = format_route_report(route)
    assert "step" in result.lower(), \
        f"❌ Report should mention 'steps', got: {result}"
    print("✅ Test 19 passed: Report contains steps label")


def test_format_report_multiple_lines():
    """Test: Multiple stops create multiple lines"""
    route = [("A", 1), ("B", 2), ("C", 3)]
    result = format_route_report(route)
    lines = result.strip().split("\n")
    assert len(lines) == 3, f"❌ Expected 3 lines, got {len(lines)}: {result}"
    print("✅ Test 20 passed: Multiple stops create multiple lines")


def run_all_tests():
    """Run all tests and show results."""
    print("=" * 50)
    print("🤖 Running Robot Patrol Route Generator Tests")
    print("=" * 50)
    print()
    
    tests = [
        test_random_waypoint_returns_tuple,
        test_random_waypoint_single_item,
        test_random_waypoint_uses_randomness,
        test_shuffle_returns_list,
        test_shuffle_contains_all_waypoints,
        test_shuffle_does_not_modify_original,
        test_shuffle_randomizes_order,
        test_generate_route_correct_length,
        test_generate_route_valid_waypoints,
        test_generate_route_zero_stops,
        test_generate_route_randomness,
        test_calculate_steps_basic,
        test_calculate_steps_single_stop,
        test_calculate_steps_empty_route,
        test_calculate_steps_with_zeros,
        test_format_report_basic,
        test_format_report_single_stop,
        test_format_report_empty_route,
        test_format_report_contains_steps_label,
        test_format_report_multiple_lines,
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
        print("🎉 All tests passed! Robot patrol route ready!")
    else:
        print("💪 Keep coding, the robot needs its route!")
    print("=" * 50)


if __name__ == "__main__":
    run_all_tests()

