import pandas as pd

import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the NHS jobs dataset.

    Args:
        df: Raw pandas DataFrame.

    Returns:
        Cleaned pandas DataFrame.
    """

    # Work on a copy
    df = df.copy()

    # Standardise column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # Remove duplicate records
    df = df.drop_duplicates()

    return df