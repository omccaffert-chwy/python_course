"""
🧪 Tests for Robot Energy Management Game

Run this file to check if your game logic is correct!

Usage:
    python tests.py

These tests automatically import your functions from project.py
and verify that your implementation is correct.
"""

from project import (
    generate_task,
    can_complete_task,
    complete_task,
    calculate_mission_score,
    get_mission_status,
    evaluate_mission_result,
    TASK_TEMPLATES,
)


# ============================================================
# GENERATE TASK TESTS
# ============================================================

def test_generate_task_returns_dict():
    """Test: Returns a dictionary"""
    result = generate_task()
    assert isinstance(result, dict), f"❌ Expected dict, got {type(result)}"
    print("✅ Test 1 passed: Returns a dictionary")


def test_generate_task_has_keys():
    """Test: Has required keys"""
    result = generate_task()
    assert "name" in result, f"❌ Missing 'name' key"
    assert "energy_cost" in result, f"❌ Missing 'energy_cost' key"
    assert "reward" in result, f"❌ Missing 'reward' key"
    print("✅ Test 2 passed: Has all required keys")


def test_generate_task_valid_name():
    """Test: Name is from valid templates"""
    valid_names = [t[0] for t in TASK_TEMPLATES]
    result = generate_task()
    assert result["name"] in valid_names, f"❌ Invalid task name: {result['name']}"
    print("✅ Test 3 passed: Task name is valid")


def test_generate_task_energy_in_range():
    """Test: Energy cost is within valid range"""
    # Run multiple times to check randomness
    for _ in range(20):
        result = generate_task()
        assert 10 <= result["energy_cost"] <= 40, \
            f"❌ Energy cost {result['energy_cost']} out of range (10-40)"
    print("✅ Test 4 passed: Energy costs are in valid range")


def test_generate_task_reward_in_range():
    """Test: Reward is within valid range"""
    for _ in range(20):
        result = generate_task()
        assert 5 <= result["reward"] <= 25, \
            f"❌ Reward {result['reward']} out of range (5-25)"
    print("✅ Test 5 passed: Rewards are in valid range")


def test_generate_task_randomness():
    """Test: Generates different tasks"""
    tasks = set()
    for _ in range(30):
        result = generate_task()
        tasks.add((result["name"], result["energy_cost"], result["reward"]))
    assert len(tasks) >= 3, f"❌ Expected variety, got only {len(tasks)} unique tasks"
    print("✅ Test 6 passed: Generates varied tasks")


# ============================================================
# CAN COMPLETE TASK TESTS
# ============================================================

def test_can_complete_enough_energy():
    """Test: Returns True when enough energy"""
    result = can_complete_task(50, 30)
    assert result == True, f"❌ Expected True (50 >= 30), got {result}"
    print("✅ Test 7 passed: True when enough energy")


def test_can_complete_not_enough():
    """Test: Returns False when not enough energy"""
    result = can_complete_task(20, 30)
    assert result == False, f"❌ Expected False (20 < 30), got {result}"
    print("✅ Test 8 passed: False when not enough energy")


def test_can_complete_exact_amount():
    """Test: Returns True when exactly enough"""
    result = can_complete_task(30, 30)
    assert result == True, f"❌ Expected True (30 >= 30), got {result}"
    print("✅ Test 9 passed: True when exactly enough energy")


def test_can_complete_zero_battery():
    """Test: Returns False when battery is zero"""
    result = can_complete_task(0, 10)
    assert result == False, f"❌ Expected False (0 < 10), got {result}"
    print("✅ Test 10 passed: False when battery is zero")


# ============================================================
# COMPLETE TASK TESTS
# ============================================================

def test_complete_task_returns_tuple():
    """Test: Returns a tuple"""
    result = complete_task(100, 25, 15)
    assert isinstance(result, tuple), f"❌ Expected tuple, got {type(result)}"
    assert len(result) == 2, f"❌ Expected 2 elements, got {len(result)}"
    print("✅ Test 11 passed: Returns a tuple of 2 elements")


def test_complete_task_battery_deduction():
    """Test: Correctly deducts battery"""
    result = complete_task(100, 25, 15)
    assert result[0] == 75, f"❌ Expected battery 75 (100-25), got {result[0]}"
    print("✅ Test 12 passed: Correctly deducts battery")


def test_complete_task_reward_returned():
    """Test: Returns correct reward"""
    result = complete_task(100, 25, 15)
    assert result[1] == 15, f"❌ Expected reward 15, got {result[1]}"
    print("✅ Test 13 passed: Returns correct reward")


def test_complete_task_different_values():
    """Test: Works with different values"""
    result = complete_task(50, 20, 10)
    assert result == (30, 10), f"❌ Expected (30, 10), got {result}"
    print("✅ Test 14 passed: Works with different values")


# ============================================================
# CALCULATE MISSION SCORE TESTS
# ============================================================

def test_calculate_score_basic():
    """Test: Calculates sum of rewards"""
    tasks = [{"reward": 10}, {"reward": 15}, {"reward": 8}]
    result = calculate_mission_score(tasks)
    assert result == 33, f"❌ Expected 33 (10+15+8), got {result}"
    print("✅ Test 15 passed: Calculates sum correctly")


def test_calculate_score_empty():
    """Test: Returns 0 for empty list"""
    result = calculate_mission_score([])
    assert result == 0, f"❌ Expected 0 for empty list, got {result}"
    print("✅ Test 16 passed: Returns 0 for empty list")


def test_calculate_score_single():
    """Test: Works with single task"""
    tasks = [{"reward": 25}]
    result = calculate_mission_score(tasks)
    assert result == 25, f"❌ Expected 25, got {result}"
    print("✅ Test 17 passed: Works with single task")


def test_calculate_score_ignores_other_keys():
    """Test: Only sums reward values"""
    tasks = [
        {"name": "Task1", "energy_cost": 20, "reward": 15},
        {"name": "Task2", "energy_cost": 30, "reward": 20}
    ]
    result = calculate_mission_score(tasks)
    assert result == 35, f"❌ Expected 35, got {result}"
    print("✅ Test 18 passed: Only sums reward values")


# ============================================================
# GET MISSION STATUS TESTS
# ============================================================

def test_status_depleted():
    """Test: Battery depleted message"""
    result = get_mission_status(0, 3)
    assert "depleted" in result.lower(), f"❌ Expected 'depleted' message, got '{result}'"
    print("✅ Test 19 passed: Battery depleted message")


def test_status_critical():
    """Test: Critical battery warning"""
    result = get_mission_status(10, 2)
    assert "critical" in result.lower(), f"❌ Expected 'critical' message, got '{result}'"
    print("✅ Test 20 passed: Critical battery warning")


def test_status_low():
    """Test: Low battery warning"""
    result = get_mission_status(20, 2)
    assert "low" in result.lower(), f"❌ Expected 'low' warning, got '{result}'"
    print("✅ Test 21 passed: Low battery warning")


def test_status_started():
    """Test: Mission started message"""
    result = get_mission_status(100, 0)
    assert "started" in result.lower() or "ready" in result.lower(), \
        f"❌ Expected 'started' or 'ready' message, got '{result}'"
    print("✅ Test 22 passed: Mission started message")


def test_status_in_progress():
    """Test: Mission in progress message"""
    result = get_mission_status(60, 4)
    assert "4" in result and ("progress" in result.lower() or "done" in result.lower()), \
        f"❌ Expected progress message with '4', got '{result}'"
    print("✅ Test 23 passed: Mission in progress message")


# ============================================================
# EVALUATE MISSION RESULT TESTS
# ============================================================

def test_evaluate_returns_dict():
    """Test: Returns a dictionary"""
    result = evaluate_mission_result([{"reward": 20}], 50, False)
    assert isinstance(result, dict), f"❌ Expected dict, got {type(result)}"
    print("✅ Test 24 passed: Returns a dictionary")


def test_evaluate_has_keys():
    """Test: Has all required keys"""
    result = evaluate_mission_result([{"reward": 20}], 50, False)
    assert "status" in result, f"❌ Missing 'status' key"
    assert "tasks_completed" in result, f"❌ Missing 'tasks_completed' key"
    assert "total_score" in result, f"❌ Missing 'total_score' key"
    assert "rating" in result, f"❌ Missing 'rating' key"
    print("✅ Test 25 passed: Has all required keys")


def test_evaluate_failure():
    """Test: Failed mission gets F rating"""
    result = evaluate_mission_result([{"reward": 50}], 0, True)
    assert result["status"] == "FAILURE", f"❌ Expected FAILURE status"
    assert result["rating"] == "F", f"❌ Expected F rating for failure"
    print("✅ Test 26 passed: Failed mission gets F rating")


def test_evaluate_s_rating():
    """Test: High score + battery gets S rating"""
    tasks = [{"reward": 30}, {"reward": 35}]  # 65 points
    result = evaluate_mission_result(tasks, 25, False)
    assert result["rating"] == "S", f"❌ Expected S rating (65 pts, 25 battery), got {result['rating']}"
    print("✅ Test 27 passed: High performance gets S rating")


def test_evaluate_a_rating():
    """Test: Good score gets A rating"""
    tasks = [{"reward": 25}, {"reward": 22}]  # 47 points
    result = evaluate_mission_result(tasks, 10, False)
    assert result["rating"] == "A", f"❌ Expected A rating (47 pts), got {result['rating']}"
    print("✅ Test 28 passed: Good score gets A rating")


def test_evaluate_b_rating():
    """Test: Moderate score gets B rating"""
    tasks = [{"reward": 15}, {"reward": 18}]  # 33 points
    result = evaluate_mission_result(tasks, 10, False)
    assert result["rating"] == "B", f"❌ Expected B rating (33 pts), got {result['rating']}"
    print("✅ Test 29 passed: Moderate score gets B rating")


def test_evaluate_c_rating():
    """Test: Low score gets C rating"""
    tasks = [{"reward": 10}, {"reward": 8}]  # 18 points
    result = evaluate_mission_result(tasks, 10, False)
    assert result["rating"] == "C", f"❌ Expected C rating (18 pts), got {result['rating']}"
    print("✅ Test 30 passed: Low score gets C rating")


def test_evaluate_task_count():
    """Test: Correctly counts tasks"""
    tasks = [{"reward": 10}, {"reward": 15}, {"reward": 20}]
    result = evaluate_mission_result(tasks, 30, False)
    assert result["tasks_completed"] == 3, f"❌ Expected 3 tasks, got {result['tasks_completed']}"
    print("✅ Test 31 passed: Correctly counts tasks")


def test_evaluate_total_score():
    """Test: Correctly calculates total score"""
    tasks = [{"reward": 10}, {"reward": 15}, {"reward": 20}]
    result = evaluate_mission_result(tasks, 30, False)
    assert result["total_score"] == 45, f"❌ Expected score 45, got {result['total_score']}"
    print("✅ Test 32 passed: Correctly calculates total score")


def run_all_tests():
    """Run all tests and show results."""
    print("=" * 50)
    print("🤖 Running Robot Energy Management Game Tests")
    print("=" * 50)
    print()
    
    tests = [
        test_generate_task_returns_dict,
        test_generate_task_has_keys,
        test_generate_task_valid_name,
        test_generate_task_energy_in_range,
        test_generate_task_reward_in_range,
        test_generate_task_randomness,
        test_can_complete_enough_energy,
        test_can_complete_not_enough,
        test_can_complete_exact_amount,
        test_can_complete_zero_battery,
        test_complete_task_returns_tuple,
        test_complete_task_battery_deduction,
        test_complete_task_reward_returned,
        test_complete_task_different_values,
        test_calculate_score_basic,
        test_calculate_score_empty,
        test_calculate_score_single,
        test_calculate_score_ignores_other_keys,
        test_status_depleted,
        test_status_critical,
        test_status_low,
        test_status_started,
        test_status_in_progress,
        test_evaluate_returns_dict,
        test_evaluate_has_keys,
        test_evaluate_failure,
        test_evaluate_s_rating,
        test_evaluate_a_rating,
        test_evaluate_b_rating,
        test_evaluate_c_rating,
        test_evaluate_task_count,
        test_evaluate_total_score,
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
        print("🎉 All tests passed! Mission accomplished!")
    else:
        print("💪 Keep debugging, the robot is counting on you!")
    print("=" * 50)


if __name__ == "__main__":
    run_all_tests()

