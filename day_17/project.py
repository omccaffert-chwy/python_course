"""
🤖 Git Version Control for Robot Projects

This project teaches:
- Git basics (init, add, commit, log)
- Branching and merging
- Understanding version control benefits

Your Task:
----------
This is a DOCUMENTATION project, not a coding project!
Complete the functions below that generate Git commands and explanations.

Then, ACTUALLY USE GIT:
1. Initialize a git repo in your robot project folder
2. Make at least 3 commits
3. Create and merge a feature branch

The functions here will help you understand and generate the right commands.

1. get_git_init_commands()
   - Return commands to initialize a repo

2. get_commit_commands(message)
   - Return commands to stage and commit

3. get_branch_commands(branch_name)
   - Return commands to create and switch branches

4. get_merge_commands(branch_name)
   - Return commands to merge a branch

5. generate_commit_message(action, description)
   - Generate a good commit message

6. get_git_workflow()
   - Return a complete workflow guide
"""


def get_git_init_commands():
    """
    Get the commands to initialize a new Git repository.
    
    Returns:
        A list of command strings in order:
        1. Initialize the repo
        2. Check status
    
    Example:
        get_git_init_commands() returns:
        ["git init", "git status"]
    """
    # TODO: Return the list of init commands
    pass


def get_commit_commands(message):
    """
    Get the commands to stage all changes and commit.
    
    Args:
        message: The commit message string
    
    Returns:
        A list of command strings:
        1. Stage all changes
        2. Commit with message
    
    Example:
        get_commit_commands("Add robot class")
        returns: ["git add .", 'git commit -m "Add robot class"']
    """
    # TODO: Return the list of commit commands
    pass


def get_branch_commands(branch_name):
    """
    Get commands to create and switch to a new branch.
    
    Args:
        branch_name: Name for the new branch
    
    Returns:
        A list of command strings:
        1. Create the branch
        2. Switch to it
        OR use the combined command
    
    Example:
        get_branch_commands("feature/sensors")
        returns: ["git checkout -b feature/sensors"]
        OR: ["git branch feature/sensors", "git checkout feature/sensors"]
    """
    # TODO: Return branch creation commands
    pass


def get_merge_commands(branch_name):
    """
    Get commands to merge a branch into main.
    
    Args:
        branch_name: Name of branch to merge
    
    Returns:
        A list of command strings:
        1. Switch to main branch
        2. Merge the feature branch
    
    Example:
        get_merge_commands("feature/sensors")
        returns: ["git checkout main", "git merge feature/sensors"]
    """
    # TODO: Return merge commands
    pass


def generate_commit_message(action, description):
    """
    Generate a well-formatted commit message.
    
    Good commit messages:
    - Start with a verb (Add, Fix, Update, Remove, Refactor)
    - Are concise but descriptive
    - Describe WHAT changed and WHY
    
    Args:
        action: The verb (e.g., "Add", "Fix", "Update")
        description: What was changed
    
    Returns:
        A formatted commit message string
    
    Example:
        generate_commit_message("Add", "battery monitoring to Robot class")
        returns: "Add battery monitoring to Robot class"
    """
    # TODO: Combine action and description into a commit message
    pass


def get_status_commands():
    """
    Get commands to check repository status.
    
    Returns:
        A list of useful status commands:
        - git status (current state)
        - git log --oneline (commit history)
        - git branch (list branches)
    """
    # TODO: Return list of status checking commands
    pass


def get_undo_commands():
    """
    Get commands to undo common mistakes.
    
    Returns:
        A dictionary of undo scenarios and commands:
        {
            "unstage_file": command to unstage,
            "discard_changes": command to discard changes,
            "undo_last_commit": command to undo commit (keep changes)
        }
    """
    # TODO: Return dictionary of undo commands
    pass


def get_git_workflow():
    """
    Get a complete Git workflow guide for robot projects.
    
    Returns:
        A dictionary with workflow steps:
        {
            "setup": list of initial setup commands,
            "daily_work": list of daily workflow commands,
            "feature_branch": list of feature branch commands,
            "tips": list of helpful tips
        }
    """
    # TODO: Return comprehensive workflow guide
    pass


def validate_branch_name(name):
    """
    Check if a branch name follows good conventions.
    
    Good branch names:
    - Use lowercase
    - Use hyphens, not spaces
    - Have a prefix like feature/, bugfix/, hotfix/
    - Are descriptive but not too long
    
    Args:
        name: Proposed branch name
    
    Returns:
        Tuple of (is_valid: bool, suggestion: str)
        If invalid, suggestion contains a better name
    
    Example:
        validate_branch_name("Add Sensors")
        returns: (False, "feature/add-sensors")
    """
    # TODO: Validate and suggest better branch name
    pass


def get_gitignore_content():
    """
    Generate .gitignore content for Python robot projects.
    
    Returns:
        A string with .gitignore contents, ignoring:
        - __pycache__/
        - *.pyc
        - .env
        - venv/
        - .idea/
        - *.log
    """
    # TODO: Return gitignore content string
    pass

