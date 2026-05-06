import pandas as pd
import pytest

from src.extract import extract_data


def test_extract_data_success(tmp_path):
    file_path = tmp_path / "sample.csv"

    df = pd.DataFrame({
        "Order ID": ["ORD001"],
        "Amount": [1000]
    })

    df.to_csv(file_path, index=False)

    result = extract_data(str(file_path))

    assert isinstance(result, pd.DataFrame)
    assert result.shape[0] == 1
    assert "Order ID" in result.columns


def test_extract_data_file_not_found():
    with pytest.raises(FileNotFoundError):
        extract_data("non_existing_file.csv")