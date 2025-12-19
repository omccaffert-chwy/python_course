"""
🧪 Tests for Mini Robot Control Panel

Run this file to check if your control panel logic is correct!

Usage:
    python tests.py
"""

from project import (
    create_panel_state,
    set_speed,
    set_battery_threshold,
    start_mission,
    stop_mission,
    get_status_message,
    update_battery,
    clear_warnings,
    get_panel_summary,
)


# ============================================================
# CREATE PANEL STATE TESTS
# ============================================================

def test_create_state():
    """Test: Create initial state"""
    state = create_panel_state()
    assert state["speed"] == 5, f"❌ Default speed should be 5"
    assert state["battery_threshold"] == 20, f"❌ Default threshold should be 20"
    assert state["battery_level"] == 100, f"❌ Default battery should be 100"
    assert state["mission_active"] == False, f"❌ Mission should be inactive"
    print("✅ Test 1 passed: Create initial state")


def test_create_state_has_warnings():
    """Test: State has warnings list"""
    state = create_panel_state()
    assert "warnings" in state, f"❌ State should have warnings"
    assert state["warnings"] == [], f"❌ Warnings should be empty list"
    print("✅ Test 2 passed: State has warnings")


# ============================================================
# SET SPEED TESTS
# ============================================================

def test_set_speed_valid():
    """Test: Set valid speed"""
    state = create_panel_state()
    set_speed(state, 7)
    assert state["speed"] == 7, f"❌ Speed should be 7"
    print("✅ Test 3 passed: Set valid speed")


def test_set_speed_clamp_high():
    """Test: Speed clamped to max 10"""
    state = create_panel_state()
    set_speed(state, 15)
    assert state["speed"] == 10, f"❌ Speed should be clamped to 10"
    print("✅ Test 4 passed: Clamp high speed")


def test_set_speed_clamp_low():
    """Test: Speed clamped to min 1"""
    state = create_panel_state()
    set_speed(state, 0)
    assert state["speed"] == 1, f"❌ Speed should be clamped to 1"
    print("✅ Test 5 passed: Clamp low speed")


# ============================================================
# BATTERY THRESHOLD TESTS
# ============================================================

def test_set_threshold():
    """Test: Set battery threshold"""
    state = create_panel_state()
    set_battery_threshold(state, 30)
    assert state["battery_threshold"] == 30, f"❌ Threshold should be 30"
    print("✅ Test 6 passed: Set threshold")


def test_set_threshold_clamp():
    """Test: Threshold clamped to 0-100"""
    state = create_panel_state()
    set_battery_threshold(state, 150)
    assert state["battery_threshold"] == 100, f"❌ Should clamp to 100"
    print("✅ Test 7 passed: Clamp threshold")


# ============================================================
# START MISSION TESTS
# ============================================================

def test_start_mission_success():
    """Test: Start mission successfully"""
    state = create_panel_state()
    success, msg = start_mission(state)
    assert success == True, f"❌ Should succeed"
    assert state["mission_active"] == True, f"❌ Mission should be active"
    print("✅ Test 8 passed: Start mission success")


def test_start_mission_already_active():
    """Test: Can't start when already active"""
    state = create_panel_state()
    start_mission(state)
    success, msg = start_mission(state)
    assert success == False, f"❌ Should fail when already active"
    print("✅ Test 9 passed: Can't double start")


def test_start_mission_low_battery():
    """Test: Can't start with low battery"""
    state = create_panel_state()
    state["battery_level"] = 10
    state["battery_threshold"] = 20
    success, msg = start_mission(state)
    assert success == False, f"❌ Should fail with low battery"
    print("✅ Test 10 passed: Can't start low battery")


# ============================================================
# STOP MISSION TESTS
# ============================================================

def test_stop_mission_success():
    """Test: Stop mission successfully"""
    state = create_panel_state()
    start_mission(state)
    success, msg = stop_mission(state)
    assert success == True, f"❌ Should succeed"
    assert state["mission_active"] == False, f"❌ Mission should be inactive"
    print("✅ Test 11 passed: Stop mission success")


def test_stop_mission_increments_count():
    """Test: Stop increments mission count"""
    state = create_panel_state()
    start_mission(state)
    stop_mission(state)
    assert state["mission_count"] == 1, f"❌ Mission count should be 1"
    print("✅ Test 12 passed: Increments count")


def test_stop_mission_not_active():
    """Test: Can't stop when not active"""
    state = create_panel_state()
    success, msg = stop_mission(state)
    assert success == False, f"❌ Should fail when not active"
    print("✅ Test 13 passed: Can't stop inactive")


# ============================================================
# STATUS MESSAGE TESTS
# ============================================================

def test_status_message_contains_info():
    """Test: Status message has required info"""
    state = create_panel_state()
    msg = get_status_message(state)
    assert "5" in msg or "speed" in msg.lower(), f"❌ Should contain speed"
    assert "100" in msg or "battery" in msg.lower(), f"❌ Should contain battery"
    print("✅ Test 14 passed: Status contains info")


# ============================================================
# UPDATE BATTERY TESTS
# ============================================================

def test_update_battery():
    """Test: Update battery level"""
    state = create_panel_state()
    update_battery(state, 75)
    assert state["battery_level"] == 75, f"❌ Battery should be 75"
    print("✅ Test 15 passed: Update battery")


def test_update_battery_warning():
    """Test: Low battery adds warning"""
    state = create_panel_state()
    state["battery_threshold"] = 30
    update_battery(state, 20)
    assert len(state["warnings"]) > 0, f"❌ Should have warning"
    print("✅ Test 16 passed: Low battery warning")


def test_update_battery_stops_mission():
    """Test: Zero battery stops mission"""
    state = create_panel_state()
    start_mission(state)
    update_battery(state, 0)
    assert state["mission_active"] == False, f"❌ Mission should stop at 0 battery"
    print("✅ Test 17 passed: Zero battery stops mission")


# ============================================================
# CLEAR WARNINGS TESTS
# ============================================================

def test_clear_warnings():
    """Test: Clear warnings"""
    state = create_panel_state()
    state["warnings"] = ["Warning 1", "Warning 2"]
    clear_warnings(state)
    assert state["warnings"] == [], f"❌ Warnings should be empty"
    print("✅ Test 18 passed: Clear warnings")


# ============================================================
# PANEL SUMMARY TESTS
# ============================================================

def test_summary_ready():
    """Test: Summary shows ready"""
    state = create_panel_state()
    summary = get_panel_summary(state)
    assert summary["is_ready"] == True, f"❌ Should be ready"
    assert summary["has_warnings"] == False, f"❌ Should have no warnings"
    print("✅ Test 19 passed: Summary ready")


def test_summary_not_ready():
    """Test: Summary shows not ready during mission"""
    state = create_panel_state()
    start_mission(state)
    summary = get_panel_summary(state)
    assert summary["is_ready"] == False, f"❌ Should not be ready during mission"
    print("✅ Test 20 passed: Summary not ready")


def run_all_tests():
    """Run all tests and show results."""
    print("=" * 50)
    print("🤖 Running Robot Control Panel Tests")
    print("=" * 50)
    print()
    
    tests = [
        test_create_state,
        test_create_state_has_warnings,
        test_set_speed_valid,
        test_set_speed_clamp_high,
        test_set_speed_clamp_low,
        test_set_threshold,
        test_set_threshold_clamp,
        test_start_mission_success,
        test_start_mission_already_active,
        test_start_mission_low_battery,
        test_stop_mission_success,
        test_stop_mission_increments_count,
        test_stop_mission_not_active,
        test_status_message_contains_info,
        test_update_battery,
        test_update_battery_warning,
        test_update_battery_stops_mission,
        test_clear_warnings,
        test_summary_ready,
        test_summary_not_ready,
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
        print("🎉 All tests passed! Control panel ready!")
    else:
        print("💪 Keep coding, control that robot!")
    print("=" * 50)


if __name__ == "__main__":
    run_all_tests()

