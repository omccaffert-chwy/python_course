"""
🧪 Tests for Robot Parts Collection Game

Run this file to check if your game logic is correct!

Usage:
    python tests.py
"""

from project import (
    create_game_state,
    spawn_part,
    move_robot,
    check_wall_collision,
    check_trail_collision,
    check_part_collection,
    update_game,
    get_game_summary,
)


# ============================================================
# CREATE GAME STATE TESTS
# ============================================================

def test_create_state_defaults():
    """Test: Default game state"""
    state = create_game_state(20)
    assert state["grid_size"] == 20, f"❌ Expected grid_size=20"
    assert state["robot_pos"] == (10, 10), f"❌ Expected center position (10, 10)"
    assert state["score"] == 0, f"❌ Expected score=0"
    assert state["game_over"] == False, f"❌ Expected game_over=False"
    print("✅ Test 1 passed: Default game state")


def test_create_state_custom_start():
    """Test: Custom start position"""
    state = create_game_state(20, start_pos=(5, 5))
    assert state["robot_pos"] == (5, 5), f"❌ Expected position (5, 5)"
    print("✅ Test 2 passed: Custom start position")


def test_create_state_has_trail():
    """Test: State has empty trail"""
    state = create_game_state(20)
    assert "trail" in state, f"❌ State missing 'trail'"
    assert isinstance(state["trail"], list), f"❌ Trail should be a list"
    print("✅ Test 3 passed: State has trail")


# ============================================================
# SPAWN PART TESTS
# ============================================================

def test_spawn_part_creates_position():
    """Test: Spawns a part"""
    state = create_game_state(20)
    spawn_part(state)
    assert state["part_pos"] is not None, f"❌ Part should be spawned"
    print("✅ Test 4 passed: Spawns a part")


def test_spawn_part_in_bounds():
    """Test: Part is within grid"""
    state = create_game_state(20)
    for _ in range(10):
        spawn_part(state)
        x, y = state["part_pos"]
        assert 0 <= x < 20 and 0 <= y < 20, f"❌ Part out of bounds: {state['part_pos']}"
    print("✅ Test 5 passed: Part in bounds")


def test_spawn_part_not_on_robot():
    """Test: Part doesn't spawn on robot"""
    state = create_game_state(10, start_pos=(5, 5))
    for _ in range(20):
        spawn_part(state)
        assert state["part_pos"] != state["robot_pos"], f"❌ Part spawned on robot"
    print("✅ Test 6 passed: Part not on robot")


# ============================================================
# MOVE ROBOT TESTS
# ============================================================

def test_move_right():
    """Test: Move right"""
    state = create_game_state(20, start_pos=(10, 10))
    move_robot(state, "right")
    assert state["robot_pos"] == (11, 10), f"❌ Expected (11, 10)"
    print("✅ Test 7 passed: Move right")


def test_move_left():
    """Test: Move left"""
    state = create_game_state(20, start_pos=(10, 10))
    move_robot(state, "left")
    assert state["robot_pos"] == (9, 10), f"❌ Expected (9, 10)"
    print("✅ Test 8 passed: Move left")


def test_move_up():
    """Test: Move up"""
    state = create_game_state(20, start_pos=(10, 10))
    move_robot(state, "up")
    assert state["robot_pos"] == (10, 11), f"❌ Expected (10, 11)"
    print("✅ Test 9 passed: Move up")


def test_move_down():
    """Test: Move down"""
    state = create_game_state(20, start_pos=(10, 10))
    move_robot(state, "down")
    assert state["robot_pos"] == (10, 9), f"❌ Expected (10, 9)"
    print("✅ Test 10 passed: Move down")


def test_move_adds_to_trail():
    """Test: Move adds old position to trail"""
    state = create_game_state(20, start_pos=(10, 10))
    move_robot(state, "right")
    assert (10, 10) in state["trail"], f"❌ Old position should be in trail"
    print("✅ Test 11 passed: Move adds to trail")


# ============================================================
# COLLISION TESTS
# ============================================================

def test_wall_collision_left():
    """Test: Wall collision on left"""
    state = create_game_state(20, start_pos=(-1, 10))
    assert check_wall_collision(state) == True, f"❌ Should detect left wall"
    print("✅ Test 12 passed: Left wall collision")


def test_wall_collision_right():
    """Test: Wall collision on right"""
    state = create_game_state(20, start_pos=(20, 10))
    assert check_wall_collision(state) == True, f"❌ Should detect right wall"
    print("✅ Test 13 passed: Right wall collision")


def test_wall_collision_none():
    """Test: No wall collision in center"""
    state = create_game_state(20, start_pos=(10, 10))
    assert check_wall_collision(state) == False, f"❌ Should not detect collision"
    print("✅ Test 14 passed: No wall collision")


def test_trail_collision_yes():
    """Test: Trail collision detected"""
    state = create_game_state(20, start_pos=(5, 5))
    state["trail"] = [(5, 5), (6, 5)]
    assert check_trail_collision(state) == True, f"❌ Should detect trail collision"
    print("✅ Test 15 passed: Trail collision detected")


def test_trail_collision_no():
    """Test: No trail collision"""
    state = create_game_state(20, start_pos=(10, 10))
    state["trail"] = [(5, 5), (6, 5)]
    assert check_trail_collision(state) == False, f"❌ Should not detect collision"
    print("✅ Test 16 passed: No trail collision")


# ============================================================
# PART COLLECTION TESTS
# ============================================================

def test_collect_part():
    """Test: Collecting a part"""
    state = create_game_state(20, start_pos=(5, 5))
    state["part_pos"] = (5, 5)
    state["score"] = 0
    result = check_part_collection(state)
    assert result == True, f"❌ Should detect part collection"
    assert state["score"] == 10, f"❌ Score should increase to 10"
    print("✅ Test 17 passed: Part collected")


def test_no_collection():
    """Test: No collection when not on part"""
    state = create_game_state(20, start_pos=(5, 5))
    state["part_pos"] = (10, 10)
    result = check_part_collection(state)
    assert result == False, f"❌ Should not collect part"
    print("✅ Test 18 passed: No collection")


def test_collection_clears_part():
    """Test: Collection clears part position"""
    state = create_game_state(20, start_pos=(5, 5))
    state["part_pos"] = (5, 5)
    check_part_collection(state)
    assert state["part_pos"] is None, f"❌ Part position should be None after collection"
    print("✅ Test 19 passed: Collection clears part")


# ============================================================
# UPDATE GAME TESTS
# ============================================================

def test_update_moves_robot():
    """Test: Update moves the robot"""
    state = create_game_state(20, start_pos=(10, 10))
    state["part_pos"] = (15, 15)  # Part elsewhere
    update_game(state, "right")
    assert state["robot_pos"] == (11, 10), f"❌ Robot should have moved"
    print("✅ Test 20 passed: Update moves robot")


def test_update_wall_game_over():
    """Test: Update sets game_over on wall collision"""
    state = create_game_state(20, start_pos=(19, 10))
    state["part_pos"] = (5, 5)
    update_game(state, "right")  # Moves to (20, 10) - out of bounds
    assert state["game_over"] == True, f"❌ Game should be over"
    print("✅ Test 21 passed: Wall causes game over")


def test_update_spawns_part():
    """Test: Update spawns part if none exists"""
    state = create_game_state(20, start_pos=(10, 10))
    state["part_pos"] = None
    update_game(state, "right")
    assert state["part_pos"] is not None, f"❌ Part should be spawned"
    print("✅ Test 22 passed: Update spawns part")


# ============================================================
# SUMMARY TESTS
# ============================================================

def test_summary_contains_score():
    """Test: Summary contains score"""
    state = create_game_state(20)
    state["score"] = 50
    summary = get_game_summary(state)
    assert "50" in summary, f"❌ Summary should contain score"
    print("✅ Test 23 passed: Summary contains score")


def test_summary_game_over():
    """Test: Summary shows game over"""
    state = create_game_state(20)
    state["game_over"] = True
    summary = get_game_summary(state)
    assert "over" in summary.lower() or "game over" in summary.lower(), \
        f"❌ Summary should indicate game over"
    print("✅ Test 24 passed: Summary shows game over")


def run_all_tests():
    """Run all tests and show results."""
    print("=" * 50)
    print("🤖 Running Robot Parts Collection Game Tests")
    print("=" * 50)
    print()
    
    tests = [
        test_create_state_defaults,
        test_create_state_custom_start,
        test_create_state_has_trail,
        test_spawn_part_creates_position,
        test_spawn_part_in_bounds,
        test_spawn_part_not_on_robot,
        test_move_right,
        test_move_left,
        test_move_up,
        test_move_down,
        test_move_adds_to_trail,
        test_wall_collision_left,
        test_wall_collision_right,
        test_wall_collision_none,
        test_trail_collision_yes,
        test_trail_collision_no,
        test_collect_part,
        test_no_collection,
        test_collection_clears_part,
        test_update_moves_robot,
        test_update_wall_game_over,
        test_update_spawns_part,
        test_summary_contains_score,
        test_summary_game_over,
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
        print("🎉 All tests passed! Game ready to play!")
    else:
        print("💪 Keep coding, collect those parts!")
    print("=" * 50)


if __name__ == "__main__":
    run_all_tests()

