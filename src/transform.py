import pandas as pd


def simplify_status(status: str) -> str:
    """
    Groups detailed order status values into broader categories.
    """
    if pd.isna(status):
        return "Unknown"

    status = str(status).lower()

    if "cancelled" in status:
        return "Cancelled"
    elif "pending" in status:
        return "Pending"
    elif "shipped" in status:
        return "Shipped"
    else:
        return "Other"


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans and transforms the Amazon sales dataset.

    Args:
        df (pd.DataFrame): Raw dataset.

    Returns:
        pd.DataFrame: Cleaned and transformed dataset.
    """
    df = df.copy()

    # Remove unnecessary columns if they exist
    columns_to_drop = [
        "index",
        "promotion-ids",
        "Unnamed: 22"
    ]

    df = df.drop(columns=[col for col in columns_to_drop if col in df.columns])

    # Normalize column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )

    # Convert date column
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Clean numeric columns
    df["qty"] = pd.to_numeric(df["qty"], errors="coerce").fillna(0)
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce").fillna(0)

    # Fill missing categorical values
    categorical_columns = [
        "status",
        "fulfilment",
        "sales_channel",
        "category",
        "ship_city",
        "ship_state",
        "ship_country"
    ]

    for col in categorical_columns:
        if col in df.columns:
            df[col] = df[col].fillna("Unknown")

    # Create new analytical variables
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["month_name"] = df["date"].dt.month_name()
    df["order_status_group"] = df["status"].apply(simplify_status)
    df["customer_type"] = df["b2b"].apply(lambda x: "B2B" if x is True else "B2C")

    return df