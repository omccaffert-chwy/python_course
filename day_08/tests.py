"""
🧪 Tests for Turtle Robot Grid Navigator

Run this file to check if your navigation logic is correct!

Usage:
    python tests.py
"""

from project import (
    create_robot_state,
    move_forward,
    turn_left,
    turn_right,
    is_at_boundary,
    get_path_history,
    calculate_total_distance,
)


# ============================================================
# CREATE ROBOT STATE TESTS
# ============================================================

def test_create_state_defaults():
    """Test: Default state values"""
    state = create_robot_state()
    assert state["x"] == 0, f"❌ Expected x=0, got {state['x']}"
    assert state["y"] == 0, f"❌ Expected y=0, got {state['y']}"
    assert state["heading"] == 0, f"❌ Expected heading=0, got {state['heading']}"
    print("✅ Test 1 passed: Default state values")


def test_create_state_custom():
    """Test: Custom state values"""
    state = create_robot_state(50, 100, 90)
    assert state["x"] == 50, f"❌ Expected x=50"
    assert state["y"] == 100, f"❌ Expected y=100"
    assert state["heading"] == 90, f"❌ Expected heading=90"
    print("✅ Test 2 passed: Custom state values")


def test_create_state_has_path():
    """Test: State includes path with starting position"""
    state = create_robot_state(10, 20, 0)
    assert "path" in state, f"❌ State missing 'path' key"
    assert (10, 20) in state["path"], f"❌ Path should contain starting position"
    print("✅ Test 3 passed: State includes path")


# ============================================================
# MOVE FORWARD TESTS
# ============================================================

def test_move_east():
    """Test: Move east (heading 0)"""
    state = create_robot_state(0, 0, 0)
    move_forward(state, 50)
    assert state["x"] == 50, f"❌ Expected x=50 after moving east"
    assert state["y"] == 0, f"❌ y should stay 0"
    print("✅ Test 4 passed: Move east")


def test_move_north():
    """Test: Move north (heading 90)"""
    state = create_robot_state(0, 0, 90)
    move_forward(state, 50)
    assert state["x"] == 0, f"❌ x should stay 0"
    assert state["y"] == 50, f"❌ Expected y=50 after moving north"
    print("✅ Test 5 passed: Move north")


def test_move_west():
    """Test: Move west (heading 180)"""
    state = create_robot_state(0, 0, 180)
    move_forward(state, 50)
    assert state["x"] == -50, f"❌ Expected x=-50 after moving west"
    print("✅ Test 6 passed: Move west")


def test_move_south():
    """Test: Move south (heading 270)"""
    state = create_robot_state(0, 0, 270)
    move_forward(state, 50)
    assert state["y"] == -50, f"❌ Expected y=-50 after moving south"
    print("✅ Test 7 passed: Move south")


def test_move_respects_boundary():
    """Test: Movement stops at boundary"""
    state = create_robot_state(180, 0, 0)
    move_forward(state, 100, 400)  # Would go to 280, but max is 200
    assert state["x"] <= 200, f"❌ x should not exceed boundary (200)"
    print("✅ Test 8 passed: Movement respects boundary")


def test_move_updates_path():
    """Test: Movement adds to path"""
    state = create_robot_state(0, 0, 0)
    move_forward(state, 50)
    assert len(state["path"]) == 2, f"❌ Path should have 2 entries"
    assert state["path"][-1] == (50, 0), f"❌ Last path entry should be new position"
    print("✅ Test 9 passed: Movement updates path")


# ============================================================
# TURN TESTS
# ============================================================

def test_turn_left_from_east():
    """Test: Turn left from east"""
    state = create_robot_state(0, 0, 0)
    turn_left(state)
    assert state["heading"] == 90, f"❌ Expected heading=90, got {state['heading']}"
    print("✅ Test 10 passed: Turn left from east")


def test_turn_left_wrap():
    """Test: Turn left wraps around"""
    state = create_robot_state(0, 0, 270)
    turn_left(state)
    assert state["heading"] == 0, f"❌ Expected heading=0 (wrapped), got {state['heading']}"
    print("✅ Test 11 passed: Turn left wraps")


def test_turn_right_from_east():
    """Test: Turn right from east"""
    state = create_robot_state(0, 0, 0)
    turn_right(state)
    assert state["heading"] == 270, f"❌ Expected heading=270, got {state['heading']}"
    print("✅ Test 12 passed: Turn right from east")


def test_turn_right_wrap():
    """Test: Turn right wraps around"""
    state = create_robot_state(0, 0, 90)
    turn_right(state)
    assert state["heading"] == 0, f"❌ Expected heading=0 (wrapped), got {state['heading']}"
    print("✅ Test 13 passed: Turn right wraps")


def test_four_left_turns():
    """Test: Four left turns = original heading"""
    state = create_robot_state(0, 0, 0)
    for _ in range(4):
        turn_left(state)
    assert state["heading"] == 0, f"❌ Four left turns should return to 0"
    print("✅ Test 14 passed: Four left turns")


# ============================================================
# BOUNDARY TESTS
# ============================================================

def test_boundary_at_edge():
    """Test: Detects robot at edge"""
    state = create_robot_state(195, 0, 0)
    assert is_at_boundary(state, 400) == True, f"❌ Should detect boundary at x=195"
    print("✅ Test 15 passed: Detects boundary at edge")


def test_boundary_not_at_edge():
    """Test: Not at boundary when in center"""
    state = create_robot_state(0, 0, 0)
    assert is_at_boundary(state, 400) == False, f"❌ Should not be at boundary at center"
    print("✅ Test 16 passed: Not at boundary in center")


def test_boundary_negative_edge():
    """Test: Detects negative boundary"""
    state = create_robot_state(-195, 0, 0)
    assert is_at_boundary(state, 400) == True, f"❌ Should detect boundary at x=-195"
    print("✅ Test 17 passed: Detects negative boundary")


# ============================================================
# PATH HISTORY TESTS
# ============================================================

def test_path_history_returns_list():
    """Test: Returns a list"""
    state = create_robot_state(0, 0, 0)
    path = get_path_history(state)
    assert isinstance(path, list), f"❌ Should return a list"
    print("✅ Test 18 passed: Returns a list")


def test_path_history_copy():
    """Test: Returns a copy (not reference)"""
    state = create_robot_state(0, 0, 0)
    path = get_path_history(state)
    path.append((999, 999))
    assert (999, 999) not in state["path"], f"❌ Should return a copy"
    print("✅ Test 19 passed: Returns a copy")


# ============================================================
# TOTAL DISTANCE TESTS
# ============================================================

def test_distance_simple():
    """Test: Simple horizontal distance"""
    state = {"path": [(0, 0), (3, 0)]}
    dist = calculate_total_distance(state)
    assert dist == 3.0, f"❌ Expected distance 3.0, got {dist}"
    print("✅ Test 20 passed: Simple distance")


def test_distance_multiple_segments():
    """Test: Multiple segments"""
    state = {"path": [(0, 0), (3, 0), (3, 4)]}
    dist = calculate_total_distance(state)
    assert dist == 7.0, f"❌ Expected distance 7.0 (3+4), got {dist}"
    print("✅ Test 21 passed: Multiple segments")


def test_distance_single_point():
    """Test: Single point = 0 distance"""
    state = {"path": [(0, 0)]}
    dist = calculate_total_distance(state)
    assert dist == 0.0, f"❌ Expected distance 0.0, got {dist}"
    print("✅ Test 22 passed: Single point")


def run_all_tests():
    """Run all tests and show results."""
    print("=" * 50)
    print("🤖 Running Grid Navigator Tests")
    print("=" * 50)
    print()
    
    tests = [
        test_create_state_defaults,
        test_create_state_custom,
        test_create_state_has_path,
        test_move_east,
        test_move_north,
        test_move_west,
        test_move_south,
        test_move_respects_boundary,
        test_move_updates_path,
        test_turn_left_from_east,
        test_turn_left_wrap,
        test_turn_right_from_east,
        test_turn_right_wrap,
        test_four_left_turns,
        test_boundary_at_edge,
        test_boundary_not_at_edge,
        test_boundary_negative_edge,
        test_path_history_returns_list,
        test_path_history_copy,
        test_distance_simple,
        test_distance_multiple_segments,
        test_distance_single_point,
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
            print(f"❌ {test.__doc__.split(':')[0]}: Function not implemented yet")
            failed += 1
        except Exception as e:
            print(f"❌ {test.__name__} crashed: {e}")
            failed += 1
    
    print()
    print("=" * 50)
    print(f"Results: {passed} passed, {failed} failed")
    if failed == 0:
        print("🎉 All tests passed! Navigator ready for Turtle!")
    else:
        print("💪 Keep coding, your robot needs navigation!")
    print("=" * 50)


if __name__ == "__main__":
    run_all_tests()

