## Day 1 — Commands & Syntax Cheat Sheet

### 1. Python Terminal Commands

| Command | Description |
|---|---|
| `python --version` | Displays the installed Python version. |
| `python -m pip install -r requirements.txt` | Installs project dependencies listed in `requirements.txt`. |
| `python -m pytest -v` | Runs automated tests and displays each test result in verbose mode. |
| `python src/pipeline.py` | Executes the data pipeline script. |
| `python -m pip list` | Lists installed Python packages. |

### 2. Python Fundamentals

| Syntax | Description |
|---|---|
| `import pandas as pd` | Imports Pandas using the conventional alias `pd`. |
| `from pathlib import Path` | Imports `Path` for working with file and directory paths. |
| `def function_name():` | Defines a reusable function. |
| `return value` | Returns a result from a function. |
| `if condition:` | Executes code when a condition is true. |
| `raise ValueError("message")` | Raises an error when input or data does not meet expectations. |
| `with pytest.raises(ValueError):` | Tests whether a particular error is raised. |
| `# comment` | Adds an explanatory comment that Python does not execute. |

### 3. Pandas Data Loading & Transformation

| Syntax | Description |
|---|---|
| `pd.read_csv(path)` | Loads a CSV file into a Pandas DataFrame. |
| `df.copy()` | Creates a copy of a DataFrame to avoid unintentionally modifying the original. |
| `df.columns` | Returns the column names. |
| `df["column"]` | Selects a column from a DataFrame. |
| `.astype("string")` | Converts values to Pandas' string data type. |
| `.str.strip()` | Removes leading and trailing whitespace from text. |
| `.str.lower()` | Converts text to lowercase. |
| `pd.to_numeric(column, errors="coerce")` | Converts values to numbers; invalid values become missing values (`NaN`). |
| `pd.to_datetime(column, errors="coerce", utc=True)` | Parses timestamps, converts them to UTC, and marks invalid timestamps as `NaT`. |
| `df.to_csv(path, index=False)` | Saves a DataFrame to CSV without writing the DataFrame index. |

### 4. Pandas Data Validation

| Syntax | Description |
|---|---|
| `.isna()` | Identifies missing values. |
| `.notna()` | Identifies values that are not missing. |
| `.eq(value)` | Checks which values equal a specified value. |
| `.gt(value)` | Checks which values are greater than a specified value. |
| `.lt(value)` | Checks which values are less than a specified value. |
| `.le(value)` | Checks which values are less than or equal to a specified value. |
| `.between(low, high)` | Checks whether values fall within a range, inclusive by default. |
| `&` | Combines Pandas conditions using AND, evaluated row by row. |
| `\|` | Combines Pandas conditions using OR, evaluated row by row. |
| `~condition` | Inverts a Boolean condition. |
| `.duplicated(keep=False)` | Identifies every occurrence of a duplicate value, including the first occurrence. |
| `.mask(condition, value)` | Replaces values where a condition is true. |
| `.loc[condition]` | Selects rows matching a condition. |
| `len(df)` | Returns the number of rows in a DataFrame. |
| `.value_counts()` | Counts occurrences of distinct values, useful for summarizing rejection reasons. |

### 5. File & Directory Operations

| Syntax | Description |
|---|---|
| `Path("folder/file.csv")` | Represents a file path using Python's path utilities. |
| `Path(output_dir).mkdir(parents=True, exist_ok=True)` | Creates a directory, including missing parent directories, without failing if it already exists. |
| `if __name__ == "__main__":` | Runs a block of code when the Python file is executed directly. |

### 6. Pytest — Automated Testing

| Syntax | Description |
|---|---|
| `import pytest` | Imports the Pytest testing framework. |
| `def test_something():` | Defines a test function that Pytest can discover. |
| `assert condition` | Fails the test if the condition is false. |
| `pd.DataFrame([record])` | Creates a DataFrame from a list of records for testing. |
| `record.update(overrides)` | Updates a dictionary with specified values, useful for creating test cases. |
| `pytest.raises(ValueError, match="...")` | Verifies that an expected error occurs and optionally matches its message. |

### 7. Useful Concepts Learned

- **DataFrame:** A two-dimensional table of rows and columns.
- **Data validation:** Checking whether data meets defined requirements.
- **Boolean mask:** A series of `True` and `False` values used to filter or validate rows.
- **Vectorization:** Applying operations to an entire Pandas column instead of manually looping through every row.
- **ETL pipeline:** Extracting, transforming, and loading data into a usable destination.
- **Unit test:** A small automated test that checks a specific behavior.
- **Rejection reason:** A recorded explanation for why a data record failed validation.

*Note: This cheat sheet covers commands and syntax used or introduced during Day 1. Some entries, such as `~condition`, are reference items for related Pandas operations rather than necessarily commands already used in the pipeline.*