from extract import extract_data
from validate import validate_data
from transform import transform_data
from load import load_data


RAW_DATA_PATH = "data/raw/Amazon Sale Report.csv"
PROCESSED_DATA_PATH = "data/processed"


def run_pipeline() -> None:
    """
    Runs the complete DataOps ETL pipeline.
    """
    print("Starting DataOps pipeline...")

    raw_data = extract_data(RAW_DATA_PATH)
    print(f"Raw data loaded: {raw_data.shape[0]} rows and {raw_data.shape[1]} columns.")

    validate_data(raw_data)
    print("Data validation completed successfully.")

    clean_data = transform_data(raw_data)
    print(f"Data transformed: {clean_data.shape[0]} rows and {clean_data.shape[1]} columns.")

    load_data(clean_data, PROCESSED_DATA_PATH)
    print("Processed datasets saved successfully.")

    print("Pipeline completed.")


if __name__ == "__main__":
    run_pipeline()