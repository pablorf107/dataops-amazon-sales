import pandas as pd
import pytest

from src.validate import validate_data


def test_validate_data_success():
    df = pd.DataFrame({
        "Order ID": ["ORD001"],
        "Date": ["2025-01-01"],
        "Status": ["Shipped"],
        "Fulfilment": ["Amazon"],
        "Sales Channel ": ["Amazon.in"],
        "Category": ["T-shirt"],
        "Qty": [1],
        "Amount": [500],
        "ship-city": ["Mumbai"],
        "ship-state": ["Maharashtra"],
        "ship-country": ["IN"],
        "B2B": [False]
    })

    assert validate_data(df) is True


def test_validate_data_missing_column():
    df = pd.DataFrame({
        "Order ID": ["ORD001"],
        "Date": ["2025-01-01"]
    })

    with pytest.raises(ValueError):
        validate_data(df)


def test_validate_data_empty_dataframe():
    df = pd.DataFrame(columns=[
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
    ])

    with pytest.raises(ValueError):
        validate_data(df)