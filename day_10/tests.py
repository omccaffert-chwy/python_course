"""
🧪 Tests for Robot Mission Log

Run this file to check if your logging system is correct!

Usage:
    python tests.py
"""

import os
from project import (
    create_mission_entry,
    append_mission_log,
    read_mission_log,
    parse_mission_entry,
    get_last_n_missions,
    calculate_success_rate,
    get_mission_statistics,
    clear_mission_log,
)


TEST_LOG_FILE = "test_missions.txt"


def cleanup_test_file():
    """Remove test file if it exists."""
    if os.path.exists(TEST_LOG_FILE):
        os.remove(TEST_LOG_FILE)


# ============================================================
# CREATE ENTRY TESTS
# ============================================================

def test_create_entry_basic():
    """Test: Create basic entry"""
    entry = create_mission_entry("M001", 5, 75, True)
    assert entry == "M001|5|75|True", f"❌ Expected 'M001|5|75|True', got '{entry}'"
    print("✅ Test 1 passed: Create basic entry")


def test_create_entry_failed():
    """Test: Create failed mission entry"""
    entry = create_mission_entry("M002", 3, 45, False)
    assert entry == "M002|3|45|False", f"❌ Expected 'M002|3|45|False', got '{entry}'"
    print("✅ Test 2 passed: Create failed mission entry")


# ============================================================
# APPEND AND READ TESTS
# ============================================================

def test_append_creates_file():
    """Test: Append creates file if missing"""
    cleanup_test_file()
    result = append_mission_log(TEST_LOG_FILE, "M001|5|75|True")
    assert result == True, f"❌ Append should return True"
    assert os.path.exists(TEST_LOG_FILE), f"❌ File should be created"
    cleanup_test_file()
    print("✅ Test 3 passed: Append creates file")


def test_read_log_basic():
    """Test: Read log entries"""
    cleanup_test_file()
    append_mission_log(TEST_LOG_FILE, "M001|5|75|True")
    append_mission_log(TEST_LOG_FILE, "M002|3|45|False")
    entries = read_mission_log(TEST_LOG_FILE)
    assert len(entries) == 2, f"❌ Expected 2 entries, got {len(entries)}"
    cleanup_test_file()
    print("✅ Test 4 passed: Read log entries")


def test_read_missing_file():
    """Test: Read missing file returns empty list"""
    cleanup_test_file()
    entries = read_mission_log("nonexistent_file.txt")
    assert entries == [], f"❌ Should return empty list for missing file"
    print("✅ Test 5 passed: Read missing file")


def test_read_removes_newlines():
    """Test: Read removes trailing newlines"""
    cleanup_test_file()
    append_mission_log(TEST_LOG_FILE, "M001|5|75|True")
    entries = read_mission_log(TEST_LOG_FILE)
    assert "\n" not in entries[0], f"❌ Entry should not contain newline"
    cleanup_test_file()
    print("✅ Test 6 passed: Read removes newlines")


# ============================================================
# PARSE ENTRY TESTS
# ============================================================

def test_parse_entry_basic():
    """Test: Parse entry into dict"""
    result = parse_mission_entry("M001|5|75|True")
    assert result["mission_id"] == "M001", f"❌ Wrong mission_id"
    assert result["tasks_completed"] == 5, f"❌ Wrong tasks_completed"
    assert result["energy_used"] == 75, f"❌ Wrong energy_used"
    assert result["success"] == True, f"❌ Wrong success value"
    print("✅ Test 7 passed: Parse entry")


def test_parse_entry_false():
    """Test: Parse entry with False success"""
    result = parse_mission_entry("M002|3|45|False")
    assert result["success"] == False, f"❌ Should parse 'False' as False"
    print("✅ Test 8 passed: Parse False success")


# ============================================================
# GET LAST N MISSIONS TESTS
# ============================================================

def test_get_last_n_basic():
    """Test: Get last 2 missions"""
    cleanup_test_file()
    append_mission_log(TEST_LOG_FILE, "M001|5|75|True")
    append_mission_log(TEST_LOG_FILE, "M002|3|45|False")
    append_mission_log(TEST_LOG_FILE, "M003|7|90|True")
    missions = get_last_n_missions(TEST_LOG_FILE, 2)
    assert len(missions) == 2, f"❌ Expected 2 missions"
    assert missions[-1]["mission_id"] == "M003", f"❌ Last should be M003"
    cleanup_test_file()
    print("✅ Test 9 passed: Get last 2 missions")


def test_get_last_n_more_than_exists():
    """Test: Request more than exists"""
    cleanup_test_file()
    append_mission_log(TEST_LOG_FILE, "M001|5|75|True")
    missions = get_last_n_missions(TEST_LOG_FILE, 5)
    assert len(missions) == 1, f"❌ Should return only 1 mission"
    cleanup_test_file()
    print("✅ Test 10 passed: Get more than exists")


# ============================================================
# SUCCESS RATE TESTS
# ============================================================

def test_success_rate_all_success():
    """Test: 100% success rate"""
    cleanup_test_file()
    append_mission_log(TEST_LOG_FILE, "M001|5|75|True")
    append_mission_log(TEST_LOG_FILE, "M002|3|45|True")
    rate = calculate_success_rate(TEST_LOG_FILE)
    assert rate == 1.0, f"❌ Expected 1.0, got {rate}"
    cleanup_test_file()
    print("✅ Test 11 passed: 100% success rate")


def test_success_rate_mixed():
    """Test: Mixed success rate"""
    cleanup_test_file()
    append_mission_log(TEST_LOG_FILE, "M001|5|75|True")
    append_mission_log(TEST_LOG_FILE, "M002|3|45|False")
    append_mission_log(TEST_LOG_FILE, "M003|7|90|True")
    append_mission_log(TEST_LOG_FILE, "M004|2|30|False")
    rate = calculate_success_rate(TEST_LOG_FILE)
    assert rate == 0.5, f"❌ Expected 0.5, got {rate}"
    cleanup_test_file()
    print("✅ Test 12 passed: 50% success rate")


def test_success_rate_empty():
    """Test: Empty log returns 0"""
    cleanup_test_file()
    rate = calculate_success_rate(TEST_LOG_FILE)
    assert rate == 0.0, f"❌ Expected 0.0 for empty log"
    print("✅ Test 13 passed: Empty log rate")


# ============================================================
# STATISTICS TESTS
# ============================================================

def test_statistics_basic():
    """Test: Basic statistics"""
    cleanup_test_file()
    append_mission_log(TEST_LOG_FILE, "M001|5|75|True")
    append_mission_log(TEST_LOG_FILE, "M002|3|45|False")
    stats = get_mission_statistics(TEST_LOG_FILE)
    assert stats["total_missions"] == 2, f"❌ Expected 2 missions"
    assert stats["successful_missions"] == 1, f"❌ Expected 1 success"
    assert stats["failed_missions"] == 1, f"❌ Expected 1 failure"
    assert stats["total_tasks"] == 8, f"❌ Expected 8 total tasks"
    assert stats["total_energy"] == 120, f"❌ Expected 120 energy"
    cleanup_test_file()
    print("✅ Test 14 passed: Basic statistics")


def test_statistics_averages():
    """Test: Average calculations"""
    cleanup_test_file()
    append_mission_log(TEST_LOG_FILE, "M001|4|80|True")
    append_mission_log(TEST_LOG_FILE, "M002|6|40|True")
    stats = get_mission_statistics(TEST_LOG_FILE)
    assert stats["avg_tasks_per_mission"] == 5.0, f"❌ Expected avg tasks 5.0"
    assert stats["avg_energy_per_mission"] == 60.0, f"❌ Expected avg energy 60.0"
    cleanup_test_file()
    print("✅ Test 15 passed: Averages")


def test_statistics_empty():
    """Test: Empty log statistics"""
    cleanup_test_file()
    stats = get_mission_statistics(TEST_LOG_FILE)
    assert stats["total_missions"] == 0, f"❌ Expected 0 missions"
    print("✅ Test 16 passed: Empty statistics")


# ============================================================
# CLEAR LOG TESTS
# ============================================================

def test_clear_log():
    """Test: Clear log file"""
    cleanup_test_file()
    append_mission_log(TEST_LOG_FILE, "M001|5|75|True")
    append_mission_log(TEST_LOG_FILE, "M002|3|45|False")
    clear_mission_log(TEST_LOG_FILE)
    entries = read_mission_log(TEST_LOG_FILE)
    assert len(entries) == 0, f"❌ Log should be empty after clear"
    cleanup_test_file()
    print("✅ Test 17 passed: Clear log")


def run_all_tests():
    """Run all tests and show results."""
    print("=" * 50)
    print("🤖 Running Robot Mission Log Tests")
    print("=" * 50)
    print()
    
    tests = [
        test_create_entry_basic,
        test_create_entry_failed,
        test_append_creates_file,
        test_read_log_basic,
        test_read_missing_file,
        test_read_removes_newlines,
        test_parse_entry_basic,
        test_parse_entry_false,
        test_get_last_n_basic,
        test_get_last_n_more_than_exists,
        test_success_rate_all_success,
        test_success_rate_mixed,
        test_success_rate_empty,
        test_statistics_basic,
        test_statistics_averages,
        test_statistics_empty,
        test_clear_log,
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
    
    # Final cleanup
    cleanup_test_file()
    
    print()
    print("=" * 50)
    print(f"Results: {passed} passed, {failed} failed")
    if failed == 0:
        print("🎉 All tests passed! Mission log operational!")
    else:
        print("💪 Keep coding, log those missions!")
    print("=" * 50)


if __name__ == "__main__":
    run_all_tests()

