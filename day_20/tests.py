"""
🧪 Tests for Capstone Project

Run this file to check your capstone implementation!

Note: You only need to pass tests for YOUR CHOSEN PATH.
- Path A tests: test_sim_*
- Path B tests: test_analysis_*

Usage:
    python tests.py
"""

import os
from project import (
    SimulatedRobot,
    SimulationController,
    SensorLogAnalyzer,
    Dashboard,
    create_sample_csv,
)


TEST_CSV = "test_sensor_data.csv"


def cleanup():
    if os.path.exists(TEST_CSV):
        os.remove(TEST_CSV)
    if os.path.exists("test_missions.json"):
        os.remove("test_missions.json")


# ============================================================
# PATH A: SIMULATION TESTS
# ============================================================

def test_sim_robot_init():
    """Test: SimulatedRobot initialization"""
    robot = SimulatedRobot("TestBot")
    assert robot.name == "TestBot", f"❌ Name should be TestBot"
    assert robot.x == 0, f"❌ x should be 0"
    assert robot.y == 0, f"❌ y should be 0"
    print("✅ Path A Test 1: Robot init")


def test_sim_robot_move():
    """Test: Robot movement"""
    robot = SimulatedRobot("TestBot")
    robot.heading = 0  # Facing east
    robot.move(10)
    assert robot.x == 10, f"❌ x should be 10 after move"
    print("✅ Path A Test 2: Robot move")


def test_sim_robot_turn():
    """Test: Robot turning"""
    robot = SimulatedRobot("TestBot")
    robot.turn(90)
    assert robot.heading == 90, f"❌ heading should be 90"
    print("✅ Path A Test 3: Robot turn")


def test_sim_recording():
    """Test: Mission recording"""
    robot = SimulatedRobot("TestBot")
    robot.start_recording()
    assert robot.is_recording == True, f"❌ Should be recording"
    robot.move(10)
    robot.turn(90)
    robot.stop_recording()
    assert robot.is_recording == False, f"❌ Should stop recording"
    assert len(robot.mission_log) > 0, f"❌ Should have saved mission"
    print("✅ Path A Test 4: Recording")


def test_sim_status():
    """Test: Robot status"""
    robot = SimulatedRobot("TestBot")
    status = robot.get_status()
    assert "x" in status or hasattr(status, '__iter__'), \
        f"❌ Status should have position info"
    print("✅ Path A Test 5: Status")


def test_sim_controller():
    """Test: Simulation controller"""
    controller = SimulationController()
    controller.add_robot("Scout")
    assert "Scout" in controller.robots, f"❌ Should have Scout"
    print("✅ Path A Test 6: Controller")


def test_sim_controller_select():
    """Test: Controller robot selection"""
    controller = SimulationController()
    controller.add_robot("Scout")
    controller.select_robot("Scout")
    assert controller.selected_robot is not None, f"❌ Should select robot"
    print("✅ Path A Test 7: Select robot")


# ============================================================
# PATH B: ANALYSIS TESTS
# ============================================================

def test_analysis_init():
    """Test: Analyzer initialization"""
    analyzer = SensorLogAnalyzer()
    assert analyzer.data == [], f"❌ Should start with empty data"
    print("✅ Path B Test 1: Analyzer init")


def test_analysis_load_csv():
    """Test: Load CSV data"""
    create_sample_csv(TEST_CSV)
    analyzer = SensorLogAnalyzer()
    analyzer.load_csv(TEST_CSV)
    assert len(analyzer.data) > 0, f"❌ Should load data"
    cleanup()
    print("✅ Path B Test 2: Load CSV")


def test_analysis_total_runs():
    """Test: Count total runs"""
    create_sample_csv(TEST_CSV)
    analyzer = SensorLogAnalyzer()
    analyzer.load_csv(TEST_CSV)
    total = analyzer.get_total_runs()
    assert total == 8, f"❌ Should have 8 runs, got {total}"
    cleanup()
    print("✅ Path B Test 3: Total runs")


def test_analysis_average_distance():
    """Test: Calculate average distance"""
    create_sample_csv(TEST_CSV)
    analyzer = SensorLogAnalyzer()
    analyzer.load_csv(TEST_CSV)
    avg = analyzer.get_average_distance()
    assert avg > 0, f"❌ Average should be positive"
    cleanup()
    print("✅ Path B Test 4: Average distance")


def test_analysis_robot_filter():
    """Test: Filter by robot"""
    create_sample_csv(TEST_CSV)
    analyzer = SensorLogAnalyzer()
    analyzer.load_csv(TEST_CSV)
    scout_runs = analyzer.get_runs_by_robot("Scout")
    assert len(scout_runs) == 5, f"❌ Scout should have 5 runs"
    cleanup()
    print("✅ Path B Test 5: Robot filter")


def test_analysis_error_runs():
    """Test: Get error runs"""
    create_sample_csv(TEST_CSV)
    analyzer = SensorLogAnalyzer()
    analyzer.load_csv(TEST_CSV)
    errors = analyzer.get_error_runs()
    assert len(errors) == 3, f"❌ Should have 3 runs with errors"
    cleanup()
    print("✅ Path B Test 6: Error runs")


def test_analysis_statistics():
    """Test: Calculate statistics"""
    create_sample_csv(TEST_CSV)
    analyzer = SensorLogAnalyzer()
    analyzer.load_csv(TEST_CSV)
    stats = analyzer.calculate_statistics()
    assert "total_runs" in stats, f"❌ Should have total_runs"
    assert "average_distance" in stats, f"❌ Should have average_distance"
    cleanup()
    print("✅ Path B Test 7: Statistics")


def test_analysis_report():
    """Test: Generate report"""
    create_sample_csv(TEST_CSV)
    analyzer = SensorLogAnalyzer()
    analyzer.load_csv(TEST_CSV)
    report = analyzer.generate_report()
    assert isinstance(report, str), f"❌ Report should be string"
    assert len(report) > 0, f"❌ Report should not be empty"
    cleanup()
    print("✅ Path B Test 8: Report")


def test_dashboard():
    """Test: Dashboard initialization"""
    dashboard = Dashboard()
    assert dashboard.analyzer is not None, f"❌ Should have analyzer"
    print("✅ Path B Test 9: Dashboard")


def test_dashboard_alerts():
    """Test: Dashboard alerts"""
    create_sample_csv(TEST_CSV)
    dashboard = Dashboard()
    dashboard.load_data(TEST_CSV)
    alerts = dashboard.get_alerts()
    assert isinstance(alerts, list), f"❌ Alerts should be list"
    cleanup()
    print("✅ Path B Test 10: Alerts")


def run_all_tests():
    """Run all tests and show results."""
    print("=" * 60)
    print("🤖 Running Capstone Project Tests")
    print("=" * 60)
    print()
    print("Note: Complete tests for YOUR CHOSEN PATH")
    print()
    
    path_a_tests = [
        test_sim_robot_init,
        test_sim_robot_move,
        test_sim_robot_turn,
        test_sim_recording,
        test_sim_status,
        test_sim_controller,
        test_sim_controller_select,
    ]
    
    path_b_tests = [
        test_analysis_init,
        test_analysis_load_csv,
        test_analysis_total_runs,
        test_analysis_average_distance,
        test_analysis_robot_filter,
        test_analysis_error_runs,
        test_analysis_statistics,
        test_analysis_report,
        test_dashboard,
        test_dashboard_alerts,
    ]
    
    # Run Path A
    print("━" * 40)
    print("PATH A: SIMULATION")
    print("━" * 40)
    path_a_passed = 0
    path_a_failed = 0
    
    for test in path_a_tests:
        try:
            test()
            path_a_passed += 1
        except AssertionError as e:
            print(str(e))
            path_a_failed += 1
        except TypeError as e:
            print(f"❌ {test.__doc__.split(':')[0]}: Not implemented")
            path_a_failed += 1
        except Exception as e:
            print(f"❌ {test.__name__}: {e}")
            path_a_failed += 1
    
    print()
    
    # Run Path B
    print("━" * 40)
    print("PATH B: DATA ANALYSIS")
    print("━" * 40)
    path_b_passed = 0
    path_b_failed = 0
    
    for test in path_b_tests:
        try:
            test()
            path_b_passed += 1
        except AssertionError as e:
            print(str(e))
            path_b_failed += 1
        except TypeError as e:
            print(f"❌ {test.__doc__.split(':')[0]}: Not implemented")
            path_b_failed += 1
        except Exception as e:
            print(f"❌ {test.__name__}: {e}")
            path_b_failed += 1
    
    cleanup()
    
    print()
    print("=" * 60)
    print("RESULTS")
    print("=" * 60)
    print(f"Path A (Simulation): {path_a_passed}/{len(path_a_tests)} passed")
    print(f"Path B (Analysis):   {path_b_passed}/{len(path_b_tests)} passed")
    print()
    
    if path_a_passed == len(path_a_tests):
        print("🎉 PATH A COMPLETE! Great simulation work!")
    elif path_b_passed == len(path_b_tests):
        print("🎉 PATH B COMPLETE! Great analysis work!")
    elif path_a_passed > 0 or path_b_passed > 0:
        print("💪 Good progress! Keep working on your chosen path!")
    else:
        print("🚀 Get started by implementing functions in project.py!")
    
    print("=" * 60)


if __name__ == "__main__":
    run_all_tests()

