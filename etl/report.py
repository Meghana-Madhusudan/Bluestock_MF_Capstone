"""
report.py

Generate ETL validation reports.
"""

from datetime import datetime
from pathlib import Path

import pandas as pd


def generate_validation_report(
    df: pd.DataFrame,
    dataset_name: str,
    report_path: Path,
    duplicate_rows_removed: int = 0,
    invalid_nav_count: int = 0,
    invalid_date_count: int = 0,
    status: str = "SUCCESS",
) -> None:
    """
    Generate a reusable validation report.
    """

    report_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    report = []

    report.append("=" * 60)
    report.append("ETL VALIDATION REPORT")
    report.append("=" * 60)

    report.append(f"Dataset       : {dataset_name}")
    report.append(
        f"Generated On  : {datetime.now():%Y-%m-%d %H:%M:%S}"
    )

    report.append("")
    report.append(f"Rows          : {len(df)}")
    report.append(f"Columns       : {len(df.columns)}")

    report.append("")
    report.append(f"Status        : {status}")

    report.append("")
    report.append("Validation Summary")
    report.append("-" * 30)
    report.append(
        f"Duplicate Rows Removed : {duplicate_rows_removed}"
    )
    report.append(
        f"Invalid Dates          : {invalid_date_count}"
    )

    if "nav" in df.columns:
        report.append(
            f"Invalid NAV Values     : {invalid_nav_count}"
        )

    report.append("")
    report.append("Missing Values")
    report.append("-" * 30)

    missing = df.isna().sum()

    for column, count in missing.items():
        report.append(f"{column:<25} {count}")

    if "date" in df.columns:

        report.append("")
        report.append("Date Range")
        report.append("-" * 30)

        report.append(f"Start Date : {df['date'].min()}")
        report.append(f"End Date   : {df['date'].max()}")

    report.append("")
    report.append("Data Types")
    report.append("-" * 30)

    for column, dtype in df.dtypes.items():
        report.append(f"{column:<25} {dtype}")

    with open(
        report_path,
        "w",
        encoding="utf-8",
    ) as file:

        file.write("\n".join(map(str, report)))

    print(f"📄 Validation report saved to: {report_path}")