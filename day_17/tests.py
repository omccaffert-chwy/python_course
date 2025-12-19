"""
🧪 Tests for Git Version Control Guide

Run this file to check if your Git guide is correct!

Usage:
    python tests.py
"""

from project import (
    get_git_init_commands,
    get_commit_commands,
    get_branch_commands,
    get_merge_commands,
    generate_commit_message,
    get_status_commands,
    get_undo_commands,
    get_git_workflow,
    validate_branch_name,
    get_gitignore_content,
)


# ============================================================
# INIT COMMANDS TESTS
# ============================================================

def test_init_commands():
    """Test: Init commands include git init"""
    commands = get_git_init_commands()
    assert isinstance(commands, list), f"❌ Should return a list"
    assert any("git init" in cmd for cmd in commands), \
        f"❌ Should include 'git init'"
    print("✅ Test 1 passed: Init commands")


# ============================================================
# COMMIT COMMANDS TESTS
# ============================================================

def test_commit_commands():
    """Test: Commit commands are correct"""
    commands = get_commit_commands("Test message")
    assert isinstance(commands, list), f"❌ Should return a list"
    assert any("git add" in cmd for cmd in commands), \
        f"❌ Should include staging command"
    assert any("git commit" in cmd and "Test message" in cmd for cmd in commands), \
        f"❌ Should include commit with message"
    print("✅ Test 2 passed: Commit commands")


def test_commit_message_quoted():
    """Test: Commit message is properly quoted"""
    commands = get_commit_commands("Add new feature")
    commit_cmd = [c for c in commands if "commit" in c][0]
    assert '"' in commit_cmd or "'" in commit_cmd, \
        f"❌ Commit message should be quoted"
    print("✅ Test 3 passed: Message quoted")


# ============================================================
# BRANCH COMMANDS TESTS
# ============================================================

def test_branch_commands():
    """Test: Branch commands create branch"""
    commands = get_branch_commands("feature/test")
    assert isinstance(commands, list), f"❌ Should return a list"
    combined = " ".join(commands)
    assert "feature/test" in combined, f"❌ Should include branch name"
    print("✅ Test 4 passed: Branch commands")


# ============================================================
# MERGE COMMANDS TESTS
# ============================================================

def test_merge_commands():
    """Test: Merge commands are correct"""
    commands = get_merge_commands("feature/test")
    assert isinstance(commands, list), f"❌ Should return a list"
    combined = " ".join(commands)
    assert "main" in combined or "master" in combined, \
        f"❌ Should switch to main branch"
    assert "merge" in combined, f"❌ Should include merge command"
    print("✅ Test 5 passed: Merge commands")


# ============================================================
# COMMIT MESSAGE TESTS
# ============================================================

def test_generate_message():
    """Test: Generate commit message"""
    msg = generate_commit_message("Add", "robot sensors")
    assert "Add" in msg, f"❌ Should include action"
    assert "robot sensors" in msg or "sensors" in msg, \
        f"❌ Should include description"
    print("✅ Test 6 passed: Generate message")


def test_message_not_empty():
    """Test: Message is not empty"""
    msg = generate_commit_message("Fix", "bug in movement")
    assert len(msg) > 5, f"❌ Message should not be too short"
    print("✅ Test 7 passed: Message not empty")


# ============================================================
# STATUS COMMANDS TESTS
# ============================================================

def test_status_commands():
    """Test: Status commands included"""
    commands = get_status_commands()
    assert isinstance(commands, list), f"❌ Should return a list"
    combined = " ".join(commands)
    assert "status" in combined, f"❌ Should include git status"
    print("✅ Test 8 passed: Status commands")


# ============================================================
# UNDO COMMANDS TESTS
# ============================================================

def test_undo_commands():
    """Test: Undo commands dictionary"""
    undo = get_undo_commands()
    assert isinstance(undo, dict), f"❌ Should return a dictionary"
    assert "unstage_file" in undo or len(undo) > 0, \
        f"❌ Should have undo commands"
    print("✅ Test 9 passed: Undo commands")


# ============================================================
# WORKFLOW TESTS
# ============================================================

def test_workflow_structure():
    """Test: Workflow has required sections"""
    workflow = get_git_workflow()
    assert isinstance(workflow, dict), f"❌ Should return a dictionary"
    assert len(workflow) >= 2, f"❌ Should have multiple sections"
    print("✅ Test 10 passed: Workflow structure")


def test_workflow_has_setup():
    """Test: Workflow includes setup"""
    workflow = get_git_workflow()
    assert "setup" in workflow or any("init" in str(v).lower() for v in workflow.values()), \
        f"❌ Should include setup section"
    print("✅ Test 11 passed: Workflow has setup")


# ============================================================
# BRANCH NAME VALIDATION TESTS
# ============================================================

def test_validate_good_name():
    """Test: Good branch name passes"""
    valid, suggestion = validate_branch_name("feature/add-sensors")
    assert valid == True, f"❌ 'feature/add-sensors' should be valid"
    print("✅ Test 12 passed: Good name valid")


def test_validate_bad_name():
    """Test: Bad branch name fails"""
    valid, suggestion = validate_branch_name("Add Sensors")
    assert valid == False, f"❌ 'Add Sensors' should be invalid"
    assert suggestion is not None, f"❌ Should provide suggestion"
    print("✅ Test 13 passed: Bad name invalid")


def test_validate_suggestion():
    """Test: Suggestion is better"""
    valid, suggestion = validate_branch_name("My New Feature")
    if not valid:
        assert " " not in suggestion, f"❌ Suggestion shouldn't have spaces"
        assert suggestion.islower() or "/" in suggestion, \
            f"❌ Suggestion should be lowercase or have prefix"
    print("✅ Test 14 passed: Better suggestion")


# ============================================================
# GITIGNORE TESTS
# ============================================================

def test_gitignore_content():
    """Test: Gitignore has Python ignores"""
    content = get_gitignore_content()
    assert isinstance(content, str), f"❌ Should return a string"
    assert "__pycache__" in content, f"❌ Should ignore __pycache__"
    assert ".pyc" in content or "*.pyc" in content, \
        f"❌ Should ignore .pyc files"
    print("✅ Test 15 passed: Gitignore content")


def test_gitignore_has_env():
    """Test: Gitignore ignores env files"""
    content = get_gitignore_content()
    assert ".env" in content or "venv" in content, \
        f"❌ Should ignore environment files"
    print("✅ Test 16 passed: Gitignore has env")


def run_all_tests():
    """Run all tests and show results."""
    print("=" * 50)
    print("🤖 Running Git Guide Tests")
    print("=" * 50)
    print()
    
    tests = [
        test_init_commands,
        test_commit_commands,
        test_commit_message_quoted,
        test_branch_commands,
        test_merge_commands,
        test_generate_message,
        test_message_not_empty,
        test_status_commands,
        test_undo_commands,
        test_workflow_structure,
        test_workflow_has_setup,
        test_validate_good_name,
        test_validate_bad_name,
        test_validate_suggestion,
        test_gitignore_content,
        test_gitignore_has_env,
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
        print("🎉 All tests passed! Now go use Git for real!")
    else:
        print("💪 Keep coding, master that version control!")
    print("=" * 50)


if __name__ == "__main__":
    run_all_tests()

