from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent

RAW_DATA = PROJECT_ROOT / "data" / "raw" / "jobs_raw.csv"

# Cleaning options
CLEANING_OPTIONS = {
    "REMOVE_DUPLICATES": True,
    "STANDARDISE_COLUMNS": True,
    "DROP_EMPTY_ROWS": False,
    "CONVERT_DATES": True,
    "CONVERT_SALARY": True,
}