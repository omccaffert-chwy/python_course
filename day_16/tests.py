"""
🧪 Tests for Robot Environment Info Fetcher

Run this file to check if your environment fetcher is correct!

Usage:
    python tests.py
"""

from project import (
    parse_weather_response,
    is_safe_for_outdoor_operation,
    parse_sunrise_sunset_response,
    is_daytime,
    get_operation_mode,
    create_environment_report,
    get_robot_recommendation,
    MOCK_WEATHER_SUNNY,
    MOCK_WEATHER_RAINY,
    MOCK_WEATHER_EXTREME,
    MOCK_SUNRISE_SUNSET,
)


# ============================================================
# PARSE WEATHER TESTS
# ============================================================

def test_parse_weather_sunny():
    """Test: Parse sunny weather"""
    result = parse_weather_response(MOCK_WEATHER_SUNNY)
    assert result["condition"] == "Clear", f"❌ Expected 'Clear', got {result.get('condition')}"
    assert result["temperature"] == 72, f"❌ Expected temp 72"
    print("✅ Test 1 passed: Parse sunny weather")


def test_parse_weather_rainy():
    """Test: Parse rainy weather"""
    result = parse_weather_response(MOCK_WEATHER_RAINY)
    assert result["condition"] == "Rain", f"❌ Expected 'Rain'"
    assert result["humidity"] == 90, f"❌ Expected humidity 90"
    print("✅ Test 2 passed: Parse rainy weather")


def test_parse_weather_has_all_fields():
    """Test: Parsed weather has all required fields"""
    result = parse_weather_response(MOCK_WEATHER_SUNNY)
    required = ["condition", "description", "temperature", "humidity", "wind_speed", "location"]
    for field in required:
        assert field in result, f"❌ Missing field: {field}"
    print("✅ Test 3 passed: All fields present")


# ============================================================
# SAFETY CHECK TESTS
# ============================================================

def test_safe_sunny():
    """Test: Sunny weather is safe"""
    weather = parse_weather_response(MOCK_WEATHER_SUNNY)
    safe, reason = is_safe_for_outdoor_operation(weather)
    assert safe == True, f"❌ Should be safe, got reason: {reason}"
    print("✅ Test 4 passed: Sunny is safe")


def test_unsafe_rain():
    """Test: Rain is unsafe"""
    weather = parse_weather_response(MOCK_WEATHER_RAINY)
    safe, reason = is_safe_for_outdoor_operation(weather)
    assert safe == False, f"❌ Rain should be unsafe"
    assert "rain" in reason.lower(), f"❌ Reason should mention rain"
    print("✅ Test 5 passed: Rain is unsafe")


def test_unsafe_extreme():
    """Test: Extreme weather is unsafe"""
    weather = parse_weather_response(MOCK_WEATHER_EXTREME)
    safe, reason = is_safe_for_outdoor_operation(weather)
    assert safe == False, f"❌ Extreme should be unsafe"
    print("✅ Test 6 passed: Extreme is unsafe")


def test_unsafe_high_wind():
    """Test: High wind is unsafe"""
    weather = {"condition": "Clear", "wind_speed": 30, "temperature": 70}
    safe, reason = is_safe_for_outdoor_operation(weather)
    assert safe == False, f"❌ High wind should be unsafe"
    print("✅ Test 7 passed: High wind is unsafe")


def test_unsafe_temperature():
    """Test: Extreme temperature is unsafe"""
    weather = {"condition": "Clear", "wind_speed": 5, "temperature": 110}
    safe, reason = is_safe_for_outdoor_operation(weather)
    assert safe == False, f"❌ High temp should be unsafe"
    print("✅ Test 8 passed: Extreme temp is unsafe")


# ============================================================
# SUNRISE/SUNSET TESTS
# ============================================================

def test_parse_sunrise_sunset():
    """Test: Parse sunrise/sunset response"""
    result = parse_sunrise_sunset_response(MOCK_SUNRISE_SUNSET)
    assert "sunrise" in result, f"❌ Missing sunrise"
    assert "sunset" in result, f"❌ Missing sunset"
    print("✅ Test 9 passed: Parse sunrise/sunset")


# ============================================================
# DAYTIME TESTS
# ============================================================

def test_is_daytime_noon():
    """Test: Noon is daytime"""
    assert is_daytime(12) == True, f"❌ 12:00 should be daytime"
    print("✅ Test 10 passed: Noon is daytime")


def test_is_daytime_night():
    """Test: Midnight is night"""
    assert is_daytime(2) == False, f"❌ 2:00 should be night"
    print("✅ Test 11 passed: Midnight is night")


def test_is_daytime_evening():
    """Test: Late evening is night"""
    assert is_daytime(22) == False, f"❌ 22:00 should be night"
    print("✅ Test 12 passed: Evening is night")


def test_is_daytime_morning():
    """Test: Morning is daytime"""
    assert is_daytime(9) == True, f"❌ 9:00 should be daytime"
    print("✅ Test 13 passed: Morning is daytime")


# ============================================================
# OPERATION MODE TESTS
# ============================================================

def test_mode_outdoor_patrol():
    """Test: Clear day = outdoor patrol"""
    weather = parse_weather_response(MOCK_WEATHER_SUNNY)
    mode = get_operation_mode(weather, 14)
    assert mode == "outdoor_patrol", f"❌ Expected outdoor_patrol, got {mode}"
    print("✅ Test 14 passed: Outdoor patrol mode")


def test_mode_indoor():
    """Test: Rain during day = indoor tasks"""
    weather = parse_weather_response(MOCK_WEATHER_RAINY)
    mode = get_operation_mode(weather, 14)
    assert mode == "indoor_tasks", f"❌ Expected indoor_tasks, got {mode}"
    print("✅ Test 15 passed: Indoor tasks mode")


def test_mode_night():
    """Test: Night = night mode"""
    weather = parse_weather_response(MOCK_WEATHER_SUNNY)
    mode = get_operation_mode(weather, 23)
    assert mode == "night_mode", f"❌ Expected night_mode, got {mode}"
    print("✅ Test 16 passed: Night mode")


# ============================================================
# ENVIRONMENT REPORT TESTS
# ============================================================

def test_report_has_fields():
    """Test: Report has all required fields"""
    weather = parse_weather_response(MOCK_WEATHER_SUNNY)
    report = create_environment_report(weather, 12)
    required = ["is_safe_outdoor", "is_daytime", "recommended_mode"]
    for field in required:
        assert field in report, f"❌ Report missing: {field}"
    print("✅ Test 17 passed: Report has all fields")


def test_report_correct_values():
    """Test: Report has correct values"""
    weather = parse_weather_response(MOCK_WEATHER_SUNNY)
    report = create_environment_report(weather, 12)
    assert report["is_safe_outdoor"] == True, f"❌ Should be safe outdoor"
    assert report["is_daytime"] == True, f"❌ Should be daytime"
    print("✅ Test 18 passed: Report values correct")


# ============================================================
# RECOMMENDATION TESTS
# ============================================================

def test_recommendation_sunny():
    """Test: Sunny recommendation"""
    rec = get_robot_recommendation("sunny", 12)
    assert "outdoor" in rec.lower() or "patrol" in rec.lower(), \
        f"❌ Sunny midday should recommend outdoor, got: {rec}"
    print("✅ Test 19 passed: Sunny recommendation")


def test_recommendation_rainy():
    """Test: Rainy recommendation"""
    rec = get_robot_recommendation("rainy", 12)
    assert "indoor" in rec.lower() or "unsafe" in rec.lower(), \
        f"❌ Rainy should recommend indoor, got: {rec}"
    print("✅ Test 20 passed: Rainy recommendation")


def run_all_tests():
    """Run all tests and show results."""
    print("=" * 50)
    print("🤖 Running Environment Info Fetcher Tests")
    print("=" * 50)
    print()
    
    tests = [
        test_parse_weather_sunny,
        test_parse_weather_rainy,
        test_parse_weather_has_all_fields,
        test_safe_sunny,
        test_unsafe_rain,
        test_unsafe_extreme,
        test_unsafe_high_wind,
        test_unsafe_temperature,
        test_parse_sunrise_sunset,
        test_is_daytime_noon,
        test_is_daytime_night,
        test_is_daytime_evening,
        test_is_daytime_morning,
        test_mode_outdoor_patrol,
        test_mode_indoor,
        test_mode_night,
        test_report_has_fields,
        test_report_correct_values,
        test_recommendation_sunny,
        test_recommendation_rainy,
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
        print("🎉 All tests passed! Environment fetcher ready!")
    else:
        print("💪 Keep coding, check that weather!")
    print("=" * 50)


if __name__ == "__main__":
    run_all_tests()

