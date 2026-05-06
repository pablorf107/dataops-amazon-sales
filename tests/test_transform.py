import pandas as pd

from src.transform import transform_data, simplify_status


def test_simplify_status_shipped():
    assert simplify_status("Shipped - Delivered to Buyer") == "Shipped"


def test_simplify_status_cancelled():
    assert simplify_status("Cancelled") == "Cancelled"


def test_simplify_status_pending():
    assert simplify_status("Pending - Waiting for Pick Up") == "Pending"


def test_simplify_status_unknown():
    assert simplify_status(None) == "Unknown"


def test_transform_data_creates_new_columns():
    df = pd.DataFrame({
        "Order ID": ["ORD001", "ORD002"],
        "Date": ["2025-01-01", "2025-02-01"],
        "Status": ["Shipped", "Cancelled"],
        "Fulfilment": ["Amazon", "Merchant"],
        "Sales Channel ": ["Amazon.in", "Amazon.in"],
        "Category": ["T-shirt", "Shoes"],
        "Qty": [2, None],
        "Amount": [1000, None],
        "ship-city": ["Mumbai", None],
        "ship-state": ["Maharashtra", None],
        "ship-country": ["IN", None],
        "B2B": [False, True]
    })

    transformed_df = transform_data(df)

    assert "year" in transformed_df.columns
    assert "month" in transformed_df.columns
    assert "month_name" in transformed_df.columns
    assert "order_status_group" in transformed_df.columns
    assert "customer_type" in transformed_df.columns


def test_transform_data_handles_missing_values():
    df = pd.DataFrame({
        "Order ID": ["ORD001"],
        "Date": ["2025-01-01"],
        "Status": [None],
        "Fulfilment": [None],
        "Sales Channel ": [None],
        "Category": [None],
        "Qty": [None],
        "Amount": [None],
        "ship-city": [None],
        "ship-state": [None],
        "ship-country": [None],
        "B2B": [False]
    })

    transformed_df = transform_data(df)

    assert transformed_df["qty"].iloc[0] == 0
    assert transformed_df["amount"].iloc[0] == 0
    assert transformed_df["status"].iloc[0] == "Unknown"
    assert transformed_df["customer_type"].iloc[0] == "B2C"