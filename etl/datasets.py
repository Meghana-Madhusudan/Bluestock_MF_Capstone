"""
datasets.py

Dataset registry for the ETL framework.

Each dataset defines:
- Expected schema
- Transformation pipeline
- Validation pipeline

The pipeline engine reads this registry instead of using
hard-coded if/else statements.
"""

from etl.transform import (
    standardize_column_names,
    strip_whitespace,
    convert_to_datetime,
    convert_numeric_columns,
    remove_duplicate_records,
    sort_dataframe,
)

from etl.validate import (
    validate_not_empty,
    validate_columns,
)


DATASET_CONFIG = {

    "01_fund_master.csv": {

        "expected_columns": [
            "amfi_code",
            "fund_house",
            "scheme_name",
            "category",
            "sub_category",
            "plan",
            "launch_date",
            "benchmark",
            "expense_ratio_pct",
            "exit_load_pct",
            "min_sip_amount",
            "min_lumpsum_amount",
            "fund_manager",
            "risk_category",
            "sebi_category_code",
        ],

        "transformations": [

            standardize_column_names,

            lambda df: convert_to_datetime(
                df,
                ["launch_date"],
            ),

            lambda df: convert_numeric_columns(
                df,
                [
                    "expense_ratio_pct",
                    "exit_load_pct",
                    "min_sip_amount",
                    "min_lumpsum_amount",
                ],
            ),

            remove_duplicate_records,
        ],

        "validations": [
            validate_not_empty,
        ],
    },

    "02_nav_history.csv": {

        "expected_columns": [
            "amfi_code",
            "date",
            "nav",
        ],

        "transformations": [

            standardize_column_names,

            lambda df: convert_to_datetime(
                df,
                ["date"],
            ),

            lambda df: convert_numeric_columns(
                df,
                ["nav"],
            ),

            remove_duplicate_records,

            lambda df: sort_dataframe(
                df,
                ["amfi_code", "date"],
            ),
        ],

        "validations": [
            validate_not_empty,
        ],
    },

    "03_aum_by_fund_house.csv": {

    "expected_columns": [
        "date",
        "fund_house",
        "aum_lakh_crore",
        "aum_crore",
        "num_schemes",
    ],

    "transformations": [

        standardize_column_names,

        lambda df: convert_to_datetime(
            df,
            ["date"],
        ),

        lambda df: convert_numeric_columns(
            df,
            [
                "aum_lakh_crore",
                "aum_crore",
                "num_schemes",
            ],
        ),

        remove_duplicate_records,

        lambda df: sort_dataframe(
            df,
            ["date", "fund_house"],
        ),
    ],

    "validations": [
        validate_not_empty,
    ],
    },

    "04_monthly_sip_inflows.csv": {

    "expected_columns": [
        "month",
        "sip_inflow_crore",
        "active_sip_accounts_crore",
        "new_sip_accounts_lakh",
        "sip_aum_lakh_crore",
        "yoy_growth_pct",
    ],

    "transformations": [

        standardize_column_names,

        strip_whitespace,

        lambda df: convert_to_datetime(
            df,
            ["month"],
            "%Y-%m",
        ),

        lambda df: convert_numeric_columns(
            df,
            [
                "sip_inflow_crore",
                "active_sip_accounts_crore",
                "new_sip_accounts_lakh",
                "sip_aum_lakh_crore",
                "yoy_growth_pct",
            ],
        ),

        remove_duplicate_records,

        lambda df: sort_dataframe(
            df,
            ["month"],
        ),
    ],

    "validations": [
        validate_not_empty,
    ],
    },

}


def get_dataset_config(dataset_name: str) -> dict:
    """
    Return configuration for a dataset.
    """

    if dataset_name not in DATASET_CONFIG:
        raise ValueError(
            f"No configuration found for {dataset_name}"
        )

    return DATASET_CONFIG[dataset_name]