"""
🧪 Tests for Robust Robot Config Loader

Run this file to check if your config loader is correct!

Usage:
    python tests.py
"""

import os
import json
from project import (
    load_json_file,
    validate_config,
    get_config_value,
    apply_defaults,
    load_robot_config,
    save_config,
    merge_configs,
    validate_value_types,
    ConfigError,
    DEFAULT_CONFIG,
)


TEST_CONFIG_FILE = "test_config.json"


def create_test_config(data):
    """Create a test config file."""
    with open(TEST_CONFIG_FILE, 'w') as f:
        json.dump(data, f)


def create_invalid_json():
    """Create an invalid JSON file."""
    with open(TEST_CONFIG_FILE, 'w') as f:
        f.write("{ invalid json }")


def cleanup_test_file():
    """Remove test file if it exists."""
    if os.path.exists(TEST_CONFIG_FILE):
        os.remove(TEST_CONFIG_FILE)


# ============================================================
# LOAD JSON FILE TESTS
# ============================================================

def test_load_json_valid():
    """Test: Load valid JSON file"""
    create_test_config({"name": "TestBot"})
    result = load_json_file(TEST_CONFIG_FILE)
    assert result["name"] == "TestBot", f"❌ Should load name"
    cleanup_test_file()
    print("✅ Test 1 passed: Load valid JSON")


def test_load_json_missing():
    """Test: Load missing file raises error"""
    cleanup_test_file()
    try:
        load_json_file("nonexistent.json")
        assert False, "❌ Should raise FileNotFoundError"
    except FileNotFoundError:
        pass
    print("✅ Test 2 passed: Missing file raises error")


def test_load_json_invalid():
    """Test: Load invalid JSON raises error"""
    create_invalid_json()
    try:
        load_json_file(TEST_CONFIG_FILE)
        assert False, "❌ Should raise JSONDecodeError"
    except json.JSONDecodeError:
        pass
    cleanup_test_file()
    print("✅ Test 3 passed: Invalid JSON raises error")


# ============================================================
# VALIDATE CONFIG TESTS
# ============================================================

def test_validate_valid():
    """Test: Valid config passes"""
    config = {"name": "Bot", "battery_capacity": 100}
    result = validate_config(config)
    assert result == True, f"❌ Should return True"
    print("✅ Test 4 passed: Valid config passes")


def test_validate_missing_name():
    """Test: Missing name raises ConfigError"""
    try:
        validate_config({"battery_capacity": 100})
        assert False, "❌ Should raise ConfigError"
    except ConfigError as e:
        assert "name" in str(e).lower(), f"❌ Error should mention 'name'"
    print("✅ Test 5 passed: Missing name raises error")


def test_validate_missing_battery():
    """Test: Missing battery_capacity raises ConfigError"""
    try:
        validate_config({"name": "Bot"})
        assert False, "❌ Should raise ConfigError"
    except ConfigError as e:
        assert "battery" in str(e).lower(), f"❌ Error should mention battery"
    print("✅ Test 6 passed: Missing battery raises error")


# ============================================================
# GET CONFIG VALUE TESTS
# ============================================================

def test_get_value_exists():
    """Test: Get existing value"""
    config = {"name": "Bot", "speed": 7}
    result = get_config_value(config, "speed", 5)
    assert result == 7, f"❌ Should return 7"
    print("✅ Test 7 passed: Get existing value")


def test_get_value_default():
    """Test: Get default for missing value"""
    config = {"name": "Bot"}
    result = get_config_value(config, "speed", 5)
    assert result == 5, f"❌ Should return default 5"
    print("✅ Test 8 passed: Get default value")


# ============================================================
# APPLY DEFAULTS TESTS
# ============================================================

def test_apply_defaults():
    """Test: Apply default values"""
    config = {"name": "Bot", "battery_capacity": 100}
    result = apply_defaults(config)
    assert result["speed"] == 5, f"❌ Should have default speed"
    assert result["sensors"] == [], f"❌ Should have default sensors"
    assert result["enabled"] == True, f"❌ Should have default enabled"
    print("✅ Test 9 passed: Apply defaults")


def test_apply_defaults_no_overwrite():
    """Test: Defaults don't overwrite existing"""
    config = {"name": "Bot", "battery_capacity": 100, "speed": 10}
    result = apply_defaults(config)
    assert result["speed"] == 10, f"❌ Should keep existing speed 10"
    print("✅ Test 10 passed: Defaults don't overwrite")


# ============================================================
# LOAD ROBOT CONFIG TESTS
# ============================================================

def test_load_config_success():
    """Test: Load complete config"""
    create_test_config({"name": "TestBot", "battery_capacity": 80})
    config, errors = load_robot_config(TEST_CONFIG_FILE)
    assert config["name"] == "TestBot", f"❌ Should load name"
    assert len(errors) == 0, f"❌ Should have no errors"
    cleanup_test_file()
    print("✅ Test 11 passed: Load config success")


def test_load_config_missing_file():
    """Test: Missing file returns defaults with error"""
    cleanup_test_file()
    config, errors = load_robot_config("nonexistent.json")
    assert config == DEFAULT_CONFIG, f"❌ Should return defaults"
    assert len(errors) > 0, f"❌ Should have error message"
    print("✅ Test 12 passed: Missing file returns defaults")


def test_load_config_invalid_json():
    """Test: Invalid JSON returns defaults with error"""
    create_invalid_json()
    config, errors = load_robot_config(TEST_CONFIG_FILE)
    assert config == DEFAULT_CONFIG, f"❌ Should return defaults"
    assert len(errors) > 0, f"❌ Should have error message"
    cleanup_test_file()
    print("✅ Test 13 passed: Invalid JSON returns defaults")


# ============================================================
# SAVE CONFIG TESTS
# ============================================================

def test_save_config():
    """Test: Save config to file"""
    cleanup_test_file()
    config = {"name": "SavedBot", "battery_capacity": 100}
    result = save_config(TEST_CONFIG_FILE, config)
    assert result == True, f"❌ Should return True"
    assert os.path.exists(TEST_CONFIG_FILE), f"❌ File should exist"
    # Verify content
    with open(TEST_CONFIG_FILE) as f:
        loaded = json.load(f)
    assert loaded["name"] == "SavedBot", f"❌ Should save name"
    cleanup_test_file()
    print("✅ Test 14 passed: Save config")


# ============================================================
# MERGE CONFIGS TESTS
# ============================================================

def test_merge_configs():
    """Test: Merge two configs"""
    base = {"name": "Bot", "speed": 5, "enabled": True}
    override = {"speed": 10}
    result = merge_configs(base, override)
    assert result["name"] == "Bot", f"❌ Should keep base name"
    assert result["speed"] == 10, f"❌ Should override speed"
    print("✅ Test 15 passed: Merge configs")


def test_merge_doesnt_modify_original():
    """Test: Merge doesn't modify originals"""
    base = {"name": "Bot", "speed": 5}
    override = {"speed": 10}
    merge_configs(base, override)
    assert base["speed"] == 5, f"❌ Should not modify base"
    print("✅ Test 16 passed: Merge preserves originals")


# ============================================================
# VALIDATE TYPES TESTS
# ============================================================

def test_validate_types_valid():
    """Test: Valid types return empty list"""
    config = {"name": "Bot", "battery_capacity": 100, "speed": 5, 
              "sensors": [], "enabled": True}
    errors = validate_value_types(config)
    assert errors == [], f"❌ Should have no errors"
    print("✅ Test 17 passed: Valid types pass")


def test_validate_types_invalid():
    """Test: Invalid types return error list"""
    config = {"name": 123, "battery_capacity": "100"}
    errors = validate_value_types(config)
    assert len(errors) >= 2, f"❌ Should have at least 2 errors"
    print("✅ Test 18 passed: Invalid types detected")


def run_all_tests():
    """Run all tests and show results."""
    print("=" * 50)
    print("🤖 Running Robust Config Loader Tests")
    print("=" * 50)
    print()
    
    tests = [
        test_load_json_valid,
        test_load_json_missing,
        test_load_json_invalid,
        test_validate_valid,
        test_validate_missing_name,
        test_validate_missing_battery,
        test_get_value_exists,
        test_get_value_default,
        test_apply_defaults,
        test_apply_defaults_no_overwrite,
        test_load_config_success,
        test_load_config_missing_file,
        test_load_config_invalid_json,
        test_save_config,
        test_merge_configs,
        test_merge_doesnt_modify_original,
        test_validate_types_valid,
        test_validate_types_invalid,
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
        print("🎉 All tests passed! Config loader robust!")
    else:
        print("💪 Keep coding, handle those errors!")
    print("=" * 50)


if __name__ == "__main__":
    run_all_tests()

