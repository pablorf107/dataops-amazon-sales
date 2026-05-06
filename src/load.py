import pandas as pd
from pathlib import Path


def load_data(df: pd.DataFrame, output_dir: str) -> None:
    """
    Saves cleaned and aggregated datasets.

    Args:
        df (pd.DataFrame): Cleaned dataset.
        output_dir (str): Directory where processed files will be saved.
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Clean dataset
    df.to_csv(output_path / "amazon_sales_clean.csv", index=False)

    # Aggregated datasets
    sales_by_month = (
        df.groupby(["year", "month"], as_index=False)
        .agg(total_sales=("amount", "sum"), total_orders=("order_id", "nunique"))
        .sort_values(["year", "month"])
    )

    sales_by_category = (
        df.groupby("category", as_index=False)
        .agg(total_sales=("amount", "sum"), total_quantity=("qty", "sum"))
        .sort_values("total_sales", ascending=False)
    )

    sales_by_state = (
        df.groupby("ship_state", as_index=False)
        .agg(total_sales=("amount", "sum"), total_orders=("order_id", "nunique"))
        .sort_values("total_sales", ascending=False)
    )

    sales_by_status = (
        df.groupby("order_status_group", as_index=False)
        .agg(total_orders=("order_id", "nunique"), total_sales=("amount", "sum"))
        .sort_values("total_orders", ascending=False)
    )

    sales_by_month.to_csv(output_path / "sales_by_month.csv", index=False)
    sales_by_category.to_csv(output_path / "sales_by_category.csv", index=False)
    sales_by_state.to_csv(output_path / "sales_by_state.csv", index=False)
    sales_by_status.to_csv(output_path / "sales_by_status.csv", index=False)