"""
🧪 Tests for Robot Sensor Log Analyzer

Run this file to check if your analyzer is correct!

Usage:
    python tests.py
"""

import os
import pandas as pd
from project import (
    load_sensor_log,
    get_column_names,
    get_run_count,
    get_average_distance,
    get_total_distance,
    get_low_battery_runs,
    get_battery_consumption,
    get_error_summary,
    get_runs_with_errors,
    generate_report,
)


TEST_CSV_FILE = "test_sensor_log.csv"


def create_test_csv():
    """Create a test CSV file."""
    data = """run_id,timestamp,distance,battery_start,battery_end,errors
R001,2024-01-15 09:00,150.5,100,75,0
R002,2024-01-15 10:30,200.2,100,45,1
R003,2024-01-15 14:00,175.8,80,25,0
R004,2024-01-16 09:00,120.0,100,60,2
R005,2024-01-16 11:00,180.5,90,40,0
"""
    with open(TEST_CSV_FILE, 'w') as f:
        f.write(data)


def cleanup_test_file():
    """Remove test file if it exists."""
    if os.path.exists(TEST_CSV_FILE):
        os.remove(TEST_CSV_FILE)


# ============================================================
# LOAD CSV TESTS
# ============================================================

def test_load_csv():
    """Test: Load CSV file"""
    create_test_csv()
    df = load_sensor_log(TEST_CSV_FILE)
    assert df is not None, f"❌ Should load CSV"
    assert isinstance(df, pd.DataFrame), f"❌ Should return DataFrame"
    cleanup_test_file()
    print("✅ Test 1 passed: Load CSV")


def test_load_missing_csv():
    """Test: Load missing file returns None"""
    cleanup_test_file()
    df = load_sensor_log("nonexistent.csv")
    assert df is None, f"❌ Should return None for missing file"
    print("✅ Test 2 passed: Handle missing file")


# ============================================================
# COLUMN NAMES TESTS
# ============================================================

def test_get_columns():
    """Test: Get column names"""
    create_test_csv()
    df = load_sensor_log(TEST_CSV_FILE)
    cols = get_column_names(df)
    assert "run_id" in cols, f"❌ Should have 'run_id' column"
    assert "distance" in cols, f"❌ Should have 'distance' column"
    assert len(cols) == 6, f"❌ Should have 6 columns"
    cleanup_test_file()
    print("✅ Test 3 passed: Get columns")


# ============================================================
# RUN COUNT TESTS
# ============================================================

def test_run_count():
    """Test: Count runs"""
    create_test_csv()
    df = load_sensor_log(TEST_CSV_FILE)
    count = get_run_count(df)
    assert count == 5, f"❌ Expected 5 runs, got {count}"
    cleanup_test_file()
    print("✅ Test 4 passed: Run count")


# ============================================================
# DISTANCE TESTS
# ============================================================

def test_average_distance():
    """Test: Average distance"""
    create_test_csv()
    df = load_sensor_log(TEST_CSV_FILE)
    avg = get_average_distance(df)
    expected = round((150.5 + 200.2 + 175.8 + 120.0 + 180.5) / 5, 2)
    assert avg == expected, f"❌ Expected {expected}, got {avg}"
    cleanup_test_file()
    print("✅ Test 5 passed: Average distance")


def test_total_distance():
    """Test: Total distance"""
    create_test_csv()
    df = load_sensor_log(TEST_CSV_FILE)
    total = get_total_distance(df)
    expected = 150.5 + 200.2 + 175.8 + 120.0 + 180.5
    assert total == expected, f"❌ Expected {expected}, got {total}"
    cleanup_test_file()
    print("✅ Test 6 passed: Total distance")


# ============================================================
# BATTERY TESTS
# ============================================================

def test_low_battery_runs():
    """Test: Get low battery runs"""
    create_test_csv()
    df = load_sensor_log(TEST_CSV_FILE)
    low = get_low_battery_runs(df, 30)
    assert len(low) == 1, f"❌ Expected 1 low battery run (R003), got {len(low)}"
    cleanup_test_file()
    print("✅ Test 7 passed: Low battery runs")


def test_low_battery_threshold():
    """Test: Low battery with higher threshold"""
    create_test_csv()
    df = load_sensor_log(TEST_CSV_FILE)
    low = get_low_battery_runs(df, 50)
    # R002 (45), R003 (25), R005 (40) are below 50
    assert len(low) == 3, f"❌ Expected 3 runs below 50, got {len(low)}"
    cleanup_test_file()
    print("✅ Test 8 passed: Low battery threshold")


def test_battery_consumption():
    """Test: Battery consumption calculation"""
    create_test_csv()
    df = load_sensor_log(TEST_CSV_FILE)
    consumption = get_battery_consumption(df)
    # R001: 100-75=25, R002: 100-45=55, R003: 80-25=55, R004: 100-60=40, R005: 90-40=50
    assert consumption.iloc[0] == 25, f"❌ First consumption should be 25"
    assert consumption.iloc[1] == 55, f"❌ Second consumption should be 55"
    cleanup_test_file()
    print("✅ Test 9 passed: Battery consumption")


# ============================================================
# ERROR TESTS
# ============================================================

def test_error_summary():
    """Test: Error summary counts"""
    create_test_csv()
    df = load_sensor_log(TEST_CSV_FILE)
    summary = get_error_summary(df)
    assert summary[0] == 3, f"❌ Expected 3 runs with 0 errors"
    assert summary[1] == 1, f"❌ Expected 1 run with 1 error"
    assert summary[2] == 1, f"❌ Expected 1 run with 2 errors"
    cleanup_test_file()
    print("✅ Test 10 passed: Error summary")


def test_runs_with_errors():
    """Test: Get runs with errors"""
    create_test_csv()
    df = load_sensor_log(TEST_CSV_FILE)
    error_runs = get_runs_with_errors(df)
    assert len(error_runs) == 2, f"❌ Expected 2 runs with errors"
    cleanup_test_file()
    print("✅ Test 11 passed: Runs with errors")


# ============================================================
# REPORT TESTS
# ============================================================

def test_report_total_runs():
    """Test: Report has total_runs"""
    create_test_csv()
    df = load_sensor_log(TEST_CSV_FILE)
    report = generate_report(df)
    assert report["total_runs"] == 5, f"❌ Expected 5 total runs"
    cleanup_test_file()
    print("✅ Test 12 passed: Report total runs")


def test_report_total_distance():
    """Test: Report has total_distance"""
    create_test_csv()
    df = load_sensor_log(TEST_CSV_FILE)
    report = generate_report(df)
    expected = 150.5 + 200.2 + 175.8 + 120.0 + 180.5
    assert report["total_distance"] == expected, f"❌ Expected {expected}"
    cleanup_test_file()
    print("✅ Test 13 passed: Report total distance")


def test_report_runs_with_errors():
    """Test: Report has runs_with_errors count"""
    create_test_csv()
    df = load_sensor_log(TEST_CSV_FILE)
    report = generate_report(df)
    assert report["runs_with_errors"] == 2, f"❌ Expected 2 runs with errors"
    cleanup_test_file()
    print("✅ Test 14 passed: Report error runs")


def run_all_tests():
    """Run all tests and show results."""
    print("=" * 50)
    print("🤖 Running Robot Sensor Log Analyzer Tests")
    print("=" * 50)
    print()
    
    tests = [
        test_load_csv,
        test_load_missing_csv,
        test_get_columns,
        test_run_count,
        test_average_distance,
        test_total_distance,
        test_low_battery_runs,
        test_low_battery_threshold,
        test_battery_consumption,
        test_error_summary,
        test_runs_with_errors,
        test_report_total_runs,
        test_report_total_distance,
        test_report_runs_with_errors,
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
        print("🎉 All tests passed! Analyzer ready!")
    else:
        print("💪 Keep coding, analyze those logs!")
    print("=" * 50)


if __name__ == "__main__":
    run_all_tests()

