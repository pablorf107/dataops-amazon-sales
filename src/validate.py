import pandas as pd


REQUIRED_COLUMNS = [
    "Order ID",
    "Date",
    "Status",
    "Fulfilment",
    "Sales Channel ",
    "Category",
    "Qty",
    "Amount",
    "ship-city",
    "ship-state",
    "ship-country",
    "B2B"
]


def validate_data(df: pd.DataFrame) -> bool:
    """
    Validates that the dataset contains the required columns.

    Args:
        df (pd.DataFrame): Raw dataset.

    Returns:
        bool: True if validation is successful.
    """
    missing_columns = [col for col in REQUIRED_COLUMNS if col not in df.columns]

    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    if df.empty:
        raise ValueError("The dataset is empty.")

    return True