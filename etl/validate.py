"""
validate.py

Reusable validation functions for the ETL pipeline.

Each validation performs a single responsibility and can be
combined to validate any dataset.
"""

import pandas as pd


def validate_not_empty(df: pd.DataFrame) -> None:
    """
    Ensure the DataFrame contains at least one row.
    """
    if df.empty:
        raise ValueError("Dataset is empty.")


def validate_columns(
    df: pd.DataFrame,
    expected_columns: list[str],
) -> None:
    """
    Raise an error if required columns are missing.
    """
    missing_columns = set(expected_columns) - set(df.columns)

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {sorted(missing_columns)}"
        )


def validate_schema(
    df: pd.DataFrame,
    expected_columns: list[str],
) -> bool:
    """
    Compare actual columns against the expected schema.

    Returns
    -------
    bool
        True if schema matches exactly.
    """

    actual_columns = list(df.columns)

    missing_columns = [
        col for col in expected_columns
        if col not in actual_columns
    ]

    extra_columns = [
        col for col in actual_columns
        if col not in expected_columns
    ]

    print("\n========== SCHEMA VALIDATION ==========")

    if missing_columns:
        print(f"❌ Missing Columns : {missing_columns}")

    if extra_columns:
        print(f"⚠️ Unexpected Columns : {extra_columns}")

    if not missing_columns and not extra_columns:
        print("✅ Schema validation passed.")
        return True

    return False


def validate_positive_values(
    df: pd.DataFrame,
    columns: list[str],
) -> dict:
    """
    Validate that numeric columns contain only positive values.

    Returns
    -------
    dict
        Number of invalid values found in each column.
    """

    results = {}

    for column in columns:

        if column not in df.columns:
            continue

        invalid_count = (df[column] <= 0).sum()

        results[column] = int(invalid_count)

    return results


def validate_missing_values(
    df: pd.DataFrame,
    columns: list[str],
) -> dict:
    """
    Count missing values in selected columns.

    Returns
    -------
    dict
    """

    results = {}

    for column in columns:

        if column not in df.columns:
            continue

        results[column] = int(df[column].isna().sum())

    return results


def validate_amfi_codes(
    nav_df: pd.DataFrame,
    fund_master_df: pd.DataFrame,
) -> None:
    """
    Ensure every AMFI code in NAV History exists
    in Fund Master.
    """

    nav_codes = set(nav_df["amfi_code"].unique())

    master_codes = set(fund_master_df["amfi_code"].unique())

    invalid_codes = nav_codes - master_codes

    print("\n" + "=" * 60)
    print("AMFI CODE VALIDATION")
    print("=" * 60)

    if not invalid_codes:

        print("✅ All AMFI Codes are valid.")
        return

    print(f"❌ Invalid AMFI Codes Found : {len(invalid_codes)}")

    print(sorted(invalid_codes))

    raise ValueError(
        "Invalid AMFI Codes found."
    )
def validate_non_negative_values(
    df: pd.DataFrame,
    columns: list[str],
) -> dict:
    """
    Validate that numeric columns contain
    only non-negative values (>= 0).

    Returns
    -------
    dict
        Number of invalid values found in each column.
    """

    results = {}

    for column in columns:

        if column not in df.columns:
            continue

        invalid_count = (df[column] < 0).sum()

        results[column] = int(invalid_count)

    return results

def run_validations(
    df: pd.DataFrame,
    validations: list,
) -> None:
    """
    Execute a sequence of validation functions.

    Example
    -------
    validations = [
        lambda df: validate_not_empty(df),
        lambda df: validate_columns(df, expected_columns),
    ]
    """

    for validation in validations:
        validation(df)