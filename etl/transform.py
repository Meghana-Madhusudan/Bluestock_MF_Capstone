"""
transform.py

Reusable data transformation functions for the ETL pipeline.

Each function:
- accepts a pandas DataFrame
- returns a transformed DataFrame
- performs ONE responsibility only

These functions are generic and reusable across multiple datasets.
"""

import pandas as pd


def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize column names.

    Example:
    NAV Date -> nav_date
    Expense Ratio (%) -> expense_ratio_pct
    """

    df = df.copy()

    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
        .str.replace("%", "pct", regex=False)
        .str.replace("/", "_", regex=False)
        .str.replace("-", "_", regex=False)
    )

    return df


def convert_to_datetime(
    df: pd.DataFrame,
    columns: list[str],
    date_format: str | None = None,
) -> pd.DataFrame:
    """
    Convert one or more columns to datetime.

    Invalid dates become NaT.
    """

    df = df.copy()

    for column in columns:
        if column in df.columns:
            df[column] = pd.to_datetime(
                df[column],
                format=date_format,
                errors="coerce",
            )

    return df


def remove_duplicate_records(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicate rows.
    """

    return df.drop_duplicates().copy()


def sort_dataframe(
    df: pd.DataFrame,
    by: list[str],
    ascending=True,
) -> pd.DataFrame:
    """
    Sort dataframe using one or more columns.
    """

    existing_columns = [col for col in by if col in df.columns]

    if not existing_columns:
        return df.copy()

    return (
        df.sort_values(
            by=existing_columns,
            ascending=ascending,
        )
        .reset_index(drop=True)
    )


def forward_fill_columns(
    df: pd.DataFrame,
    columns: list[str],
) -> pd.DataFrame:
    """
    Forward-fill selected columns.
    Useful for NAV history datasets.
    """

    df = df.copy()

    for column in columns:
        if column in df.columns:
            df[column] = df[column].ffill()

    return df


def convert_numeric_columns(
    df: pd.DataFrame,
    columns: list[str],
) -> pd.DataFrame:
    """
    Convert selected columns to numeric.

    Invalid values become NaN.
    """

    df = df.copy()

    for column in columns:
        if column in df.columns:
            df[column] = pd.to_numeric(
                df[column],
                errors="coerce",
            )

    return df


def strip_whitespace(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove leading/trailing spaces
    from all string columns.
    """

    df = df.copy()

    object_columns = df.select_dtypes(include="object").columns

    for column in object_columns:
        df[column] = df[column].str.strip()

    return df


def apply_transformations(
    df: pd.DataFrame,
    transformations: list,
) -> pd.DataFrame:
    """
    Apply a sequence of transformation functions.

    Example

    transformations = [
        lambda df: standardize_column_names(df),
        lambda df: convert_to_datetime(df, ["date"]),
        lambda df: remove_duplicate_records(df),
    ]
    """

    for transform in transformations:
        df = transform(df)

    return df