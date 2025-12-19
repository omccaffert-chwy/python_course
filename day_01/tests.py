"""
🧪 Tests for Robot Name & Battery Estimator

Run this file to check if your calculations are correct!

Usage:
    python tests.py

These tests automatically import your functions from project.py
and verify that your implementation is correct.
"""

from project import calculate_operating_hours, create_robot_name, get_robot_summary


# ============================================================
# TESTS - Run this file to check your work!
# ============================================================

def test_operating_hours_basic():
    """Test: 100 Wh battery with 25 W draw = 4 hours"""
    result = calculate_operating_hours(100, 25)
    expected = 4.0
    assert result == expected, f"❌ Expected {expected} hours, got {result}"
    print("✅ Test 1 passed: Basic calculation (100Wh / 25W = 4h)")


def test_operating_hours_decimal():
    """Test: 50 Wh battery with 15 W draw = 3.33... hours"""
    result = calculate_operating_hours(50, 15)
    expected = 50 / 15  # ~3.333...
    assert abs(result - expected) < 0.01, f"❌ Expected ~{expected:.2f} hours, got {result}"
    print("✅ Test 2 passed: Decimal result (50Wh / 15W ≈ 3.33h)")


def test_operating_hours_large_battery():
    """Test: Large battery 500 Wh with 10 W draw = 50 hours"""
    result = calculate_operating_hours(500, 10)
    expected = 50.0
    assert result == expected, f"❌ Expected {expected} hours, got {result}"
    print("✅ Test 3 passed: Large battery (500Wh / 10W = 50h)")


def test_operating_hours_high_power():
    """Test: 100 Wh battery with 100 W draw = 1 hour"""
    result = calculate_operating_hours(100, 100)
    expected = 1.0
    assert result == expected, f"❌ Expected {expected} hours, got {result}"
    print("✅ Test 4 passed: High power draw (100Wh / 100W = 1h)")


def test_robot_name_creation():
    """Test: Combining 'Scout' and '3000' = 'Scout-3000'"""
    result = create_robot_name("Scout", "3000")
    assert "Scout" in result and "3000" in result, f"❌ Robot name should contain both 'Scout' and '3000', got '{result}'"
    print(f"✅ Test 5 passed: Robot name creation ('{result}')")


def test_robot_name_different_inputs():
    """Test: Combining 'Helper' and 'X1' contains both parts"""
    result = create_robot_name("Helper", "X1")
    assert "Helper" in result and "X1" in result, f"❌ Robot name should contain both 'Helper' and 'X1', got '{result}'"
    print(f"✅ Test 6 passed: Different robot name ('{result}')")


# ============================================================
# ROBOT SUMMARY TESTS - Tests the get_robot_summary function
# ============================================================

def test_robot_summary_basic():
    """Test: Summary contains robot name and operating hours"""
    result = get_robot_summary("Scout", "3000", 100, 25)
    # Should contain the robot name (Scout-3000 or similar)
    assert "Scout" in result and "3000" in result, \
        f"❌ Summary should contain robot name parts, got '{result}'"
    # Should contain the operating hours (4.0 or 4)
    assert "4" in result, \
        f"❌ Summary should contain operating hours (4), got '{result}'"
    print("✅ Test 7 passed: Summary contains robot name and hours")


def test_robot_summary_decimal_hours():
    """Test: Summary handles decimal operating hours"""
    result = get_robot_summary("Helper", "X1", 50, 15)
    # Should contain robot name parts
    assert "Helper" in result and "X1" in result, \
        f"❌ Summary should contain robot name parts, got '{result}'"
    # Should contain operating hours (~3.33)
    assert "3" in result, \
        f"❌ Summary should contain operating hours (~3.33), got '{result}'"
    print("✅ Test 8 passed: Summary handles decimal hours")


def test_robot_summary_contains_specs():
    """Test: Summary includes battery and power information"""
    result = get_robot_summary("Buddy", "2000", 200, 40)
    # Should contain some reference to the specs or calculated result
    has_battery = "200" in result
    has_power = "40" in result
    has_hours = "5" in result  # 200/40 = 5
    has_name = "Buddy" in result and "2000" in result
    
    assert has_name, f"❌ Summary should contain robot name, got '{result}'"
    assert has_hours or (has_battery and has_power), \
        f"❌ Summary should contain specs or operating hours, got '{result}'"
    print("✅ Test 9 passed: Summary includes specs")


def run_all_tests():
    """Run all tests and show results."""
    print("=" * 50)
    print("🤖 Running Robot Name & Battery Estimator Tests")
    print("=" * 50)
    print()
    
    tests = [
        test_operating_hours_basic,
        test_operating_hours_decimal,
        test_operating_hours_large_battery,
        test_operating_hours_high_power,
        test_robot_name_creation,
        test_robot_name_different_inputs,
        test_robot_summary_basic,
        test_robot_summary_decimal_hours,
        test_robot_summary_contains_specs,
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
            # Likely the function returned None (not implemented yet)
            print(f"❌ {test.__doc__.split(':')[0]}: Function not implemented yet (returned None)")
            failed += 1
        except Exception as e:
            print(f"❌ {test.__name__} crashed: {e}")
            failed += 1
    
    print()
    print("=" * 50)
    print(f"Results: {passed} passed, {failed} failed")
    if failed == 0:
        print("🎉 All tests passed! Great work!")
    else:
        print("💪 Keep working on it, you've got this!")
    print("=" * 50)


if __name__ == "__main__":
    run_all_tests()
