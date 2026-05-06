import pandas as pd
from pathlib import Path


def extract_data(file_path: str) -> pd.DataFrame:
    """
    Reads the raw Amazon sales dataset from a CSV file.

    Args:
        file_path (str): Path to the raw CSV file.

    Returns:
        pd.DataFrame: Raw dataset.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    df = pd.read_csv(path)
    return df