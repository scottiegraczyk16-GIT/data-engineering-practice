# Day 1 — Building a Data Quality Pipeline with Python

## Overview

Built a Python-based data engineering pipeline to process synthetic computer vision image metadata. The goal was to practice loading raw data, cleaning and validating records, identifying data quality issues, and separating valid records from rejected records for downstream processing.

## Technologies Used

- **Python** — pipeline logic and data validation
- **Pandas** — data manipulation, cleaning, and transformation
- **Pytest** — automated testing and validation
- **GitHub Codespaces** — cloud-based development environment

## What I Built

### 1. Data Ingestion
- Loaded raw image metadata from a CSV file using Pandas.
- Defined required columns to ensure incoming data follows the expected schema.
- Added error handling for missing required columns.

### 2. Data Cleaning and Transformation
- Standardized text fields by trimming whitespace and converting labels to lowercase.
- Converted image dimensions and confidence scores to numeric values.
- Parsed capture timestamps into consistent UTC datetime values.
- Calculated image pixel counts using width × height.

### 3. Data Quality Validation
Implemented validation rules to identify and reject records containing:
- Missing image IDs, labels, or file paths.
- Invalid or missing capture timestamps.
- Missing, zero, or negative image dimensions.
- Image dimensions below the minimum supported size of **320 × 240 pixels**.
- Invalid confidence scores.
- Duplicate image IDs.

Each rejected record receives a rejection reason to support troubleshooting and data quality reporting.

### 4. Automated Testing
Created automated tests with Pytest to verify pipeline behavior, including:
- Valid records are cleaned and transformed correctly.
- Invalid image dimensions are rejected.
- Invalid confidence scores are rejected.
- Duplicate image IDs are identified and rejected.
- Missing required columns raise an appropriate error.

**Initial test results:** 5 tests passed. Additional tests are being added as the pipeline evolves.

## Project Structure

```text
data-engineering-practice/
├── data/
│   ├── raw/
│   │   └── image_metadata.csv
│   └── processed/
├── src/
│   ├── __init__.py
│   └── pipeline.py
├── tests/
│   └── test_pipeline.py
├── requirements.txt
└── README.md
```

## Key Takeaways

- Practiced building a reusable, function-based data pipeline.
- Learned how Pandas handles tabular data and performs vectorized validation.
- Used Boolean conditions to apply multiple data quality rules across entire columns.
- Implemented a reject-and-reason pattern for invalid data.
- Used automated tests to catch logic errors and verify expected behavior.

## Next Steps

- Add minimum image dimension validation tests.
- Generate data quality summaries using Pandas `groupby()`.
- Calculate average confidence scores by detection label.
- Report clean-record counts and rejection rates.
- Add command-line arguments to make the pipeline configurable.

*All data used in this project is synthetic and intended for educational purposes.*

