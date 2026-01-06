# Day 6 – Python Environment Setup

**Topics Covered:**

* Virtual environments (`venv`)
* Package structure (`__init__.py`)
* Installing and managing libraries (`pip`)
* Understanding PATH and environment variables

---

## 1. Virtual Environments (`venv`)

Virtual environments isolate your Python projects so each can have its own dependencies without conflicts.

### Why use them?
- Project A needs `pandas==1.5` but Project B needs `pandas==2.0`
- Keep your system Python clean
- Makes your project reproducible for others

### Commands to know:

```bash
# Create a virtual environment
python -m venv venv

# Activate it (Linux/Mac)
source venv/bin/activate

# Activate it (Windows)
venv\Scripts\activate

# Deactivate when done
deactivate

# Check which python you're using
which python
```

### Your task:
1. Navigate to the `day_06` folder
2. Create a virtual environment called `venv`
3. Activate it
4. Notice how your terminal prompt changes (shows `(venv)`)
5. Run `which python` or `where python` to see the path changed

---

## 2. Package Structure & `__init__.py`

When you want to organize code into folders (packages), Python needs to know those folders contain importable code.

### Example structure:
```
my_project/
├── main.py
└── robot/
    ├── __init__.py
    ├── sensors.py
    └── motors.py
```

### What `__init__.py` does:
- Marks a directory as a Python package
- Can be empty or contain initialization code
- Allows imports like `from robot import sensors`

### Your task:
1. Look at the `robot_package/` folder in this directory
2. Examine the `__init__.py` file
3. Run `python main.py` to see how imports work
4. Try removing `__init__.py` and see what happens

---

## 3. Installing Libraries (`pip`)

`pip` is Python's package manager for installing third-party libraries.

### Commands to know:

```bash
# Install a package
pip install requests

# Install a specific version
pip install pandas==2.0.0

# Install from requirements file
pip install -r requirements.txt

# See what's installed
pip list

# Save your dependencies
pip freeze > requirements.txt

# Uninstall a package
pip uninstall requests
```

### Your task:
1. Make sure your venv is activated
2. Install `requests` library: `pip install requests`
3. Run `pip list` to see it installed
4. Run `pip freeze > requirements.txt` to save dependencies
5. Look at the `requirements.txt` file that was created

---

## 4. Understanding PATH

PATH is an environment variable that tells your system where to find executables.

### Why it matters:
- When you type `python`, your system searches PATH to find it
- Virtual environments work by putting their `bin/` folder first in PATH
- Understanding PATH helps debug "command not found" errors

### Commands to explore:

```bash
# See your PATH (Linux/Mac)
echo $PATH

# See your PATH (Windows)
echo %PATH%

# See where python is found
which python      # Linux/Mac
where python      # Windows
```

### Your task:
1. With venv deactivated, run `which python`
2. Activate your venv, run `which python` again
3. Notice the path changed to your venv's python
4. Run `echo $PATH` and find your venv's bin folder

---

## Project Checklist

Complete these tasks and check them off:

- [ ] Created a virtual environment in `day_06/venv`
- [ ] Successfully activated and deactivated the venv
- [ ] Ran `main.py` and understood the package imports
- [ ] Installed `requests` library in your venv
- [ ] Created a `requirements.txt` file
- [ ] Understood how PATH changes with venv activation

---

## Stretch Goals

1. Create your own package with multiple modules
2. Add a function to `robot_package/sensors.py` and import it in `main.py`
3. Research the difference between `pip install` and `pip install -e .` (editable installs)

---

## Common Errors & Solutions

**"No module named 'robot_package'"**
- Make sure you're running from the `day_06` directory
- Make sure `__init__.py` exists in the package folder

**"pip: command not found"**
- Your venv might not be activated
- Try `python -m pip install` instead

**"Permission denied"**
- Don't use `sudo pip install` - use a virtual environment instead!
