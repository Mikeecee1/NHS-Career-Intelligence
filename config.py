from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent

RAW_DATA = PROJECT_ROOT / "data" / "raw" / "jobs_raw.csv"

# Cleaning options
CLEANING_OPTIONS = {
    "remove_duplicates": True,
    "standardise_columns": True,
    "drop_empty_rows": False,
    "convert_dates": True,
    "convert_salary": True,
}