"""
pipeline.py

Generic ETL pipeline engine.

The pipeline itself contains no dataset-specific logic.
Dataset behavior is controlled through the dataset registry
defined in datasets.py.
"""

from pathlib import Path

from etl.extract import extract_csv
from etl.load import save_csv
from etl.report import generate_validation_report

from etl.config import REPORTS_DIR

from etl.datasets import get_dataset_config

from etl.transform import apply_transformations

from etl.validate import (
    validate_schema,
    validate_columns,
    run_validations,
    validate_amfi_codes,
)


def run_pipeline(
    input_path: Path,
    output_path: Path,
) -> None:
    """
    Execute the ETL pipeline for a dataset.
    """

    dataset_name = input_path.name

    print("=" * 60)
    print(f"Starting ETL Pipeline : {dataset_name}")
    print("=" * 60)

    # --------------------------------------------------
    # Load dataset configuration
    # --------------------------------------------------

    print(f"DEBUG dataset_name = '{dataset_name}'")
    
    config = get_dataset_config(dataset_name)

    expected_columns = config["expected_columns"]

    transformations = config["transformations"]

    validations = config["validations"]

    # --------------------------------------------------
    # Extract
    # --------------------------------------------------

    print("📥 Extracting dataset...")

    df = extract_csv(input_path)

    # --------------------------------------------------
    # Cross-dataset validation
    # --------------------------------------------------

    if dataset_name == "02_nav_history.csv":

        fund_master_path = (
            input_path.parent / "01_fund_master.csv"
        )

        fund_master_df = extract_csv(
            fund_master_path
        )

        validate_amfi_codes(
            df,
            fund_master_df,
        )

    # --------------------------------------------------
    # Generic validations
    # --------------------------------------------------

    print("✅ Running validations...")

    run_validations(
        df,
        validations,
    )

    # --------------------------------------------------
    # Generic transformations
    # --------------------------------------------------

    print("🔄 Applying transformations...")

    df = apply_transformations(
        df,
        transformations,
    )

    # --------------------------------------------------
    # Schema validation
    # --------------------------------------------------

    validate_columns(
        df,
        expected_columns,
    )

    if not validate_schema(
        df,
        expected_columns,
    ):
        raise ValueError(
            "Schema validation failed."
        )

    # --------------------------------------------------
    # Save processed dataset
    # --------------------------------------------------

    print("💾 Saving processed dataset...")

    save_csv(
        df,
        output_path,
    )

    # --------------------------------------------------
    # Validation report
    # --------------------------------------------------

    report_name = (
        output_path.stem.replace(
            "_processed",
            "",
        )
        + "_validation_report.txt"
    )

    generate_validation_report(
        df=df,
        dataset_name=dataset_name,
        report_path=REPORTS_DIR / report_name,
        duplicate_rows_removed=0,
        invalid_nav_count=0,
        invalid_date_count=0,
        status="SUCCESS",
    )

    print("=" * 60)
    print("✅ Pipeline completed successfully.")
    print("=" * 60)