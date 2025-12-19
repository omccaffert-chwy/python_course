"""
🧪 Tests for Robot Command Translator

Run this file to check if your translator is correct!

Usage:
    python tests.py
"""

from project import (
    parse_command,
    translate_command,
    parse_command_sequence,
    translate_sequence,
    commands_to_dict,
    filter_movement_commands,
    filter_turn_commands,
    calculate_total_distance,
    get_command_summary,
)


# ============================================================
# PARSE COMMAND TESTS
# ============================================================

def test_parse_forward():
    """Test: Parse forward command"""
    result = parse_command("F10")
    assert result == ("F", 10), f"❌ Expected ('F', 10), got {result}"
    print("✅ Test 1 passed: Parse forward")


def test_parse_turn():
    """Test: Parse turn command"""
    result = parse_command("L90")
    assert result == ("L", 90), f"❌ Expected ('L', 90), got {result}"
    print("✅ Test 2 passed: Parse turn")


def test_parse_stop():
    """Test: Parse stop command (no number)"""
    result = parse_command("S")
    assert result == ("S", 0), f"❌ Expected ('S', 0), got {result}"
    print("✅ Test 3 passed: Parse stop")


def test_parse_large_number():
    """Test: Parse command with large number"""
    result = parse_command("F150")
    assert result == ("F", 150), f"❌ Expected ('F', 150), got {result}"
    print("✅ Test 4 passed: Parse large number")


# ============================================================
# TRANSLATE COMMAND TESTS
# ============================================================

def test_translate_forward():
    """Test: Translate forward"""
    result = translate_command("F10")
    assert "forward" in result.lower() and "10" in result, \
        f"❌ Should contain 'forward' and '10', got '{result}'"
    print("✅ Test 5 passed: Translate forward")


def test_translate_backward():
    """Test: Translate backward"""
    result = translate_command("B5")
    assert "backward" in result.lower() and "5" in result, \
        f"❌ Should contain 'backward' and '5', got '{result}'"
    print("✅ Test 6 passed: Translate backward")


def test_translate_left():
    """Test: Translate left turn"""
    result = translate_command("L90")
    assert "left" in result.lower() and "90" in result, \
        f"❌ Should contain 'left' and '90', got '{result}'"
    print("✅ Test 7 passed: Translate left")


def test_translate_stop():
    """Test: Translate stop"""
    result = translate_command("S")
    assert "stop" in result.lower(), f"❌ Should contain 'stop', got '{result}'"
    print("✅ Test 8 passed: Translate stop")


# ============================================================
# PARSE SEQUENCE TESTS
# ============================================================

def test_parse_sequence():
    """Test: Parse command sequence"""
    result = parse_command_sequence("F10 L90 F5")
    assert result == ["F10", "L90", "F5"], f"❌ Got {result}"
    print("✅ Test 9 passed: Parse sequence")


def test_parse_single():
    """Test: Parse single command"""
    result = parse_command_sequence("S")
    assert result == ["S"], f"❌ Got {result}"
    print("✅ Test 10 passed: Parse single")


# ============================================================
# TRANSLATE SEQUENCE TESTS
# ============================================================

def test_translate_sequence():
    """Test: Translate sequence"""
    commands = ["F10", "L90"]
    result = translate_sequence(commands)
    assert len(result) == 2, f"❌ Expected 2 translations"
    assert "forward" in result[0].lower(), f"❌ First should be forward"
    print("✅ Test 11 passed: Translate sequence")


# ============================================================
# COMMANDS TO DICT TESTS
# ============================================================

def test_commands_to_dict():
    """Test: Commands to dict"""
    commands = ["F10", "L90", "F5"]
    result = commands_to_dict(commands)
    assert result[1] == "F10", f"❌ Step 1 should be F10"
    assert result[2] == "L90", f"❌ Step 2 should be L90"
    assert result[3] == "F5", f"❌ Step 3 should be F5"
    print("✅ Test 12 passed: Commands to dict")


# ============================================================
# FILTER TESTS
# ============================================================

def test_filter_movement():
    """Test: Filter movement commands"""
    commands = ["F10", "L90", "B5", "R45", "F3"]
    result = filter_movement_commands(commands)
    assert result == ["F10", "B5", "F3"], f"❌ Got {result}"
    print("✅ Test 13 passed: Filter movement")


def test_filter_turns():
    """Test: Filter turn commands"""
    commands = ["F10", "L90", "B5", "R45"]
    result = filter_turn_commands(commands)
    assert result == ["L90", "R45"], f"❌ Got {result}"
    print("✅ Test 14 passed: Filter turns")


def test_filter_empty():
    """Test: Filter with no matches"""
    commands = ["L90", "R45"]
    result = filter_movement_commands(commands)
    assert result == [], f"❌ Expected empty list"
    print("✅ Test 15 passed: Filter empty result")


# ============================================================
# CALCULATE DISTANCE TESTS
# ============================================================

def test_distance_forward_only():
    """Test: Calculate distance forward only"""
    commands = ["F10", "L90", "F5"]
    result = calculate_total_distance(commands)
    assert result == 15, f"❌ Expected 15, got {result}"
    print("✅ Test 16 passed: Distance forward only")


def test_distance_with_backward():
    """Test: Calculate distance with backward"""
    commands = ["F10", "B3", "F5"]
    result = calculate_total_distance(commands)
    assert result == 12, f"❌ Expected 12 (10-3+5), got {result}"
    print("✅ Test 17 passed: Distance with backward")


def test_distance_negative():
    """Test: Calculate negative total distance"""
    commands = ["F5", "B10"]
    result = calculate_total_distance(commands)
    assert result == -5, f"❌ Expected -5, got {result}"
    print("✅ Test 18 passed: Negative distance")


# ============================================================
# SUMMARY TESTS
# ============================================================

def test_command_summary():
    """Test: Command summary counts"""
    commands = ["F10", "F5", "L90", "R45", "B3"]
    result = get_command_summary(commands)
    assert result["F"] == 2, f"❌ Expected F=2"
    assert result["L"] == 1, f"❌ Expected L=1"
    assert result["B"] == 1, f"❌ Expected B=1"
    print("✅ Test 19 passed: Command summary")


def test_summary_zeros():
    """Test: Summary includes zero counts"""
    commands = ["F10", "F5"]
    result = get_command_summary(commands)
    assert result["B"] == 0, f"❌ B should be 0"
    assert result["S"] == 0, f"❌ S should be 0"
    print("✅ Test 20 passed: Summary zeros")


def run_all_tests():
    """Run all tests and show results."""
    print("=" * 50)
    print("🤖 Running Robot Command Translator Tests")
    print("=" * 50)
    print()
    
    tests = [
        test_parse_forward,
        test_parse_turn,
        test_parse_stop,
        test_parse_large_number,
        test_translate_forward,
        test_translate_backward,
        test_translate_left,
        test_translate_stop,
        test_parse_sequence,
        test_parse_single,
        test_translate_sequence,
        test_commands_to_dict,
        test_filter_movement,
        test_filter_turns,
        test_filter_empty,
        test_distance_forward_only,
        test_distance_with_backward,
        test_distance_negative,
        test_command_summary,
        test_summary_zeros,
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
        print("🎉 All tests passed! Translator operational!")
    else:
        print("💪 Keep coding, translate those commands!")
    print("=" * 50)


if __name__ == "__main__":
    run_all_tests()

