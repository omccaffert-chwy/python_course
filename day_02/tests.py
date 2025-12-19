"""
🧪 Tests for Robot Safety Check System

Run this file to check if your robot logic is correct!

Usage:
    python tests.py

These tests automatically import your functions from project.py
and verify that your implementation is correct.
"""

from project import (
    normalize_input,
    check_battery_level,
    check_sensor_status,
    check_operation_mode,
    get_startup_result,
)


# ============================================================
# NORMALIZE INPUT TESTS
# ============================================================

def test_normalize_basic():
    """Test: Basic lowercase conversion"""
    result = normalize_input("ONLINE")
    assert result == "online", f"❌ Expected 'online', got '{result}'"
    print("✅ Test 1 passed: Basic lowercase (ONLINE → online)")


def test_normalize_whitespace():
    """Test: Strip whitespace and lowercase"""
    result = normalize_input("  PATROL  ")
    assert result == "patrol", f"❌ Expected 'patrol', got '{result}'"
    print("✅ Test 2 passed: Whitespace stripped (  PATROL   → patrol)")


def test_normalize_mixed():
    """Test: Mixed case with spaces"""
    result = normalize_input(" MaInTeNaNcE ")
    assert result == "maintenance", f"❌ Expected 'maintenance', got '{result}'"
    print("✅ Test 3 passed: Mixed case normalized ( MaInTeNaNcE  → maintenance)")


# ============================================================
# BATTERY LEVEL TESTS
# ============================================================

def test_battery_high():
    """Test: High battery passes"""
    result = check_battery_level(80)
    assert result == True, f"❌ Expected True for 80%, got {result}"
    print("✅ Test 4 passed: High battery (80%) passes")


def test_battery_threshold():
    """Test: Battery at threshold passes"""
    result = check_battery_level(20)
    assert result == True, f"❌ Expected True for 20%, got {result}"
    print("✅ Test 5 passed: Battery at threshold (20%) passes")


def test_battery_low():
    """Test: Low battery fails"""
    result = check_battery_level(15)
    assert result == False, f"❌ Expected False for 15%, got {result}"
    print("✅ Test 6 passed: Low battery (15%) fails")


def test_battery_critical():
    """Test: Critical battery fails"""
    result = check_battery_level(5)
    assert result == False, f"❌ Expected False for 5%, got {result}"
    print("✅ Test 7 passed: Critical battery (5%) fails")


# ============================================================
# SENSOR STATUS TESTS
# ============================================================

def test_sensor_online():
    """Test: Online sensors pass"""
    result = check_sensor_status("online")
    assert result == True, f"❌ Expected True for 'online', got {result}"
    print("✅ Test 8 passed: Online sensors pass")


def test_sensor_offline():
    """Test: Offline sensors fail"""
    result = check_sensor_status("offline")
    assert result == False, f"❌ Expected False for 'offline', got {result}"
    print("✅ Test 9 passed: Offline sensors fail")


def test_sensor_error():
    """Test: Error status fails"""
    result = check_sensor_status("error")
    assert result == False, f"❌ Expected False for 'error', got {result}"
    print("✅ Test 10 passed: Error sensors fail")


# ============================================================
# OPERATION MODE TESTS
# ============================================================

def test_mode_patrol():
    """Test: Patrol mode recognized"""
    result = check_operation_mode("patrol")
    assert result == "patrol", f"❌ Expected 'patrol', got '{result}'"
    print("✅ Test 11 passed: Patrol mode recognized")


def test_mode_charge():
    """Test: Charge mode recognized"""
    result = check_operation_mode("charge")
    assert result == "charge", f"❌ Expected 'charge', got '{result}'"
    print("✅ Test 12 passed: Charge mode recognized")


def test_mode_maintenance():
    """Test: Maintenance mode recognized"""
    result = check_operation_mode("maintenance")
    assert result == "maintenance", f"❌ Expected 'maintenance', got '{result}'"
    print("✅ Test 13 passed: Maintenance mode recognized")


def test_mode_unknown():
    """Test: Unknown mode → standby"""
    result = check_operation_mode("dance")
    assert result == "standby", f"❌ Expected 'standby' for unknown mode, got '{result}'"
    print("✅ Test 14 passed: Unknown mode → standby")


# ============================================================
# FULL STARTUP TESTS
# ============================================================

def test_startup_patrol():
    """Test: Successful patrol startup"""
    result = get_startup_result(50, "online", "patrol")
    assert "patrol" in result.lower() and "operational" in result.lower(), \
        f"❌ Expected patrol operational message, got '{result}'"
    print("✅ Test 15 passed: Patrol mode startup works")


def test_startup_battery_critical():
    """Test: Low battery stops startup"""
    result = get_startup_result(10, "online", "patrol")
    assert "battery" in result.lower() and ("critical" in result.lower() or "shut" in result.lower()), \
        f"❌ Expected battery critical message, got '{result}'"
    print("✅ Test 16 passed: Low battery → shutdown")


def test_startup_sensors_offline():
    """Test: Offline sensors stop startup"""
    result = get_startup_result(50, "offline", "patrol")
    assert "sensor" in result.lower() and ("offline" in result.lower() or "cannot" in result.lower()), \
        f"❌ Expected sensors offline message, got '{result}'"
    print("✅ Test 17 passed: Offline sensors → cannot operate")


def test_startup_charge_mode():
    """Test: Charge mode startup"""
    result = get_startup_result(50, "online", "charge")
    assert "charg" in result.lower(), \
        f"❌ Expected charging message, got '{result}'"
    print("✅ Test 18 passed: Charge mode → returning to station")


def test_startup_maintenance():
    """Test: Maintenance mode startup"""
    result = get_startup_result(50, "online", "maintenance")
    assert "maintenance" in result.lower() or "motor" in result.lower(), \
        f"❌ Expected maintenance message, got '{result}'"
    print("✅ Test 19 passed: Maintenance mode → motors disabled")


def test_startup_unknown_mode():
    """Test: Unknown mode → standby"""
    result = get_startup_result(50, "online", "dance")
    assert "standby" in result.lower() or "unknown" in result.lower(), \
        f"❌ Expected standby/unknown message, got '{result}'"
    print("✅ Test 20 passed: Unknown mode → standby")


def test_startup_case_insensitive():
    """Test: Startup handles mixed case input"""
    result = get_startup_result(50, "ONLINE", "PATROL")
    assert "patrol" in result.lower() and "operational" in result.lower(), \
        f"❌ Expected patrol operational with uppercase input, got '{result}'"
    print("✅ Test 21 passed: Case insensitive input works")


def run_all_tests():
    """Run all tests and show results."""
    print("=" * 50)
    print("🤖 Running Robot Safety Check Tests")
    print("=" * 50)
    print()
    
    tests = [
        test_normalize_basic,
        test_normalize_whitespace,
        test_normalize_mixed,
        test_battery_high,
        test_battery_threshold,
        test_battery_low,
        test_battery_critical,
        test_sensor_online,
        test_sensor_offline,
        test_sensor_error,
        test_mode_patrol,
        test_mode_charge,
        test_mode_maintenance,
        test_mode_unknown,
        test_startup_patrol,
        test_startup_battery_critical,
        test_startup_sensors_offline,
        test_startup_charge_mode,
        test_startup_maintenance,
        test_startup_unknown_mode,
        test_startup_case_insensitive,
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
        print("🎉 All systems operational! Robot ready!")
    else:
        print("💪 Keep debugging, you've got this!")
    print("=" * 50)


if __name__ == "__main__":
    run_all_tests()
