import pandas as pd

from src.load import load_data


def test_load_data_creates_processed_files(tmp_path):
    df = pd.DataFrame({
        "order_id": ["ORD001", "ORD002", "ORD003"],
        "year": [2025, 2025, 2025],
        "month": [1, 1, 2],
        "category": ["T-shirt", "Shoes", "T-shirt"],
        "amount": [1000, 500, 700],
        "qty": [2, 1, 3],
        "ship_state": ["Maharashtra", "Delhi", "Maharashtra"],
        "order_status_group": ["Shipped", "Cancelled", "Shipped"]
    })

    load_data(df, str(tmp_path))

    expected_files = [
        "amazon_sales_clean.csv",
        "sales_by_month.csv",
        "sales_by_category.csv",
        "sales_by_state.csv",
        "sales_by_status.csv"
    ]

    for file_name in expected_files:
        assert (tmp_path / file_name).exists()


def test_load_data_sales_by_category_content(tmp_path):
    df = pd.DataFrame({
        "order_id": ["ORD001", "ORD002"],
        "year": [2025, 2025],
        "month": [1, 1],
        "category": ["T-shirt", "T-shirt"],
        "amount": [1000, 500],
        "qty": [2, 1],
        "ship_state": ["Maharashtra", "Maharashtra"],
        "order_status_group": ["Shipped", "Shipped"]
    })

    load_data(df, str(tmp_path))

    sales_by_category = pd.read_csv(tmp_path / "sales_by_category.csv")

    assert sales_by_category.loc[0, "category"] == "T-shirt"
    assert sales_by_category.loc[0, "total_sales"] == 1500
    assert sales_by_category.loc[0, "total_quantity"] == 3