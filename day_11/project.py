"""
🤖 Robot Sensor Log Analyzer (CSV)

This project teaches:
- Reading CSV files with pandas
- DataFrame operations (selecting columns, filtering)
- Basic statistics (mean, sum, count)
- Data analysis workflow

Your Task:
----------
Complete the functions below to analyze robot sensor data.

1. load_sensor_log(filename)
   - Load CSV data into a pandas DataFrame

2. get_column_names(df)
   - Return list of column names

3. get_run_count(df)
   - Count total number of runs

4. get_average_distance(df)
   - Calculate average distance traveled

5. get_low_battery_runs(df, threshold)
   - Filter runs where battery dropped below threshold

6. get_error_summary(df)
   - Count errors by type

7. generate_report(df)
   - Generate a complete analysis report

Expected CSV Format:
--------------------
run_id,timestamp,distance,battery_start,battery_end,errors
R001,2024-01-15 09:00,150.5,100,75,0
R002,2024-01-15 10:30,200.2,100,45,1
R003,2024-01-15 14:00,175.8,80,30,0

Note: A sample CSV file 'sensor_log.csv' should be created for testing.
"""

import pandas as pd


def load_sensor_log(filename):
    """
    Load sensor log from a CSV file into a pandas DataFrame.
    
    Args:
        filename: Path to the CSV file
    
    Returns:
        A pandas DataFrame with the sensor data
        Returns None if file doesn't exist
    
    Example:
        df = load_sensor_log("sensor_log.csv")
        df.head()  # Shows first 5 rows
    """
    # TODO: Use pd.read_csv() to load the file
    # Handle FileNotFoundError by returning None
    pass


def get_column_names(df):
    """
    Get the column names from the DataFrame.
    
    Args:
        df: A pandas DataFrame
    
    Returns:
        A list of column name strings
    
    Example:
        get_column_names(df) -> ['run_id', 'timestamp', 'distance', ...]
    """
    # TODO: Return list of column names
    pass


def get_run_count(df):
    """
    Count the total number of runs in the log.
    
    Args:
        df: A pandas DataFrame
    
    Returns:
        Number of rows as an integer
    
    Example:
        get_run_count(df) -> 25
    """
    # TODO: Return the number of rows in the DataFrame
    pass


def get_average_distance(df):
    """
    Calculate the average distance traveled across all runs.
    
    Args:
        df: A pandas DataFrame with a 'distance' column
    
    Returns:
        Average distance as a float, rounded to 2 decimal places
    
    Example:
        get_average_distance(df) -> 175.5
    """
    # TODO: Calculate and return the mean of the 'distance' column
    pass


def get_total_distance(df):
    """
    Calculate the total distance traveled across all runs.
    
    Args:
        df: A pandas DataFrame with a 'distance' column
    
    Returns:
        Total distance as a float
    
    Example:
        get_total_distance(df) -> 4387.5
    """
    # TODO: Calculate and return the sum of the 'distance' column
    pass


def get_low_battery_runs(df, threshold=30):
    """
    Find runs where battery_end dropped below the threshold.
    
    Args:
        df: A pandas DataFrame with a 'battery_end' column
        threshold: Battery level threshold (default 30)
    
    Returns:
        A DataFrame containing only the low battery runs
    
    Example:
        low_runs = get_low_battery_runs(df, 30)
        # Returns rows where battery_end < 30
    """
    # TODO: Filter DataFrame where battery_end < threshold
    pass


def get_battery_consumption(df):
    """
    Calculate battery consumption for each run.
    
    Args:
        df: A pandas DataFrame with 'battery_start' and 'battery_end' columns
    
    Returns:
        A pandas Series with battery consumption (start - end)
    
    Example:
        consumption = get_battery_consumption(df)
        # Series: [25, 55, 50, ...]
    """
    # TODO: Return battery_start - battery_end
    pass


def get_error_summary(df):
    """
    Count runs by number of errors.
    
    Args:
        df: A pandas DataFrame with an 'errors' column
    
    Returns:
        A dictionary with error counts: {0: count, 1: count, 2: count, ...}
    
    Example:
        get_error_summary(df) -> {0: 15, 1: 8, 2: 2}
        # 15 runs with 0 errors, 8 with 1 error, etc.
    """
    # TODO: Use value_counts() on the 'errors' column
    pass


def get_runs_with_errors(df):
    """
    Get all runs that had at least one error.
    
    Args:
        df: A pandas DataFrame with an 'errors' column
    
    Returns:
        A DataFrame with only rows where errors > 0
    """
    # TODO: Filter DataFrame where errors > 0
    pass


def generate_report(df):
    """
    Generate a comprehensive analysis report.
    
    Args:
        df: A pandas DataFrame with sensor data
    
    Returns:
        A dictionary with analysis results:
        {
            "total_runs": int,
            "total_distance": float,
            "average_distance": float,
            "runs_with_errors": int,
            "low_battery_runs": int,
            "average_battery_consumption": float
        }
    
    Example:
        report = generate_report(df)
        print(report["total_runs"])  # 25
    """
    # TODO: Use other functions to compile the report
    pass

