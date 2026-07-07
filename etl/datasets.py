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

    "05_category_inflows.csv": {

    "expected_columns": [
        "month",
        "category",
        "net_inflow_crore",
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
                "net_inflow_crore",
            ],
        ),

        remove_duplicate_records,

        lambda df: sort_dataframe(
            df,
            ["month", "category"],
        ),
    ],

    "validations": [
        validate_not_empty,
    ],
    },

        "06_industry_folio_count.csv": {

    "expected_columns": [
        "month",
        "total_folios_crore",
        "equity_folios_crore",
        "debt_folios_crore",
        "hybrid_folios_crore",
        "others_folios_crore",
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
                "total_folios_crore",
                "equity_folios_crore",
                "debt_folios_crore",
                "hybrid_folios_crore",
                "others_folios_crore",
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

        "07_scheme_performance.csv": {

        "expected_columns": [
            "amfi_code",
            "scheme_name",
            "fund_house",
            "category",
            "plan",
            "return_1yr_pct",
            "return_3yr_pct",
            "return_5yr_pct",
            "benchmark_3yr_pct",
            "alpha",
            "beta",
            "sharpe_ratio",
            "sortino_ratio",
            "std_dev_ann_pct",
            "max_drawdown_pct",
            "aum_crore",
            "expense_ratio_pct",
            "morningstar_rating",
            "risk_grade",
        ],

        "transformations": [

            standardize_column_names,

            strip_whitespace,

            lambda df: convert_numeric_columns(
                df,
                [
                    "amfi_code",
                    "return_1yr_pct",
                    "return_3yr_pct",
                    "return_5yr_pct",
                    "benchmark_3yr_pct",
                    "alpha",
                    "beta",
                    "sharpe_ratio",
                    "sortino_ratio",
                    "std_dev_ann_pct",
                    "max_drawdown_pct",
                    "aum_crore",
                    "expense_ratio_pct",
                    "morningstar_rating",
                ],
            ),

            remove_duplicate_records,

            lambda df: sort_dataframe(
                df,
                ["fund_house", "scheme_name"],
            ),
        ],

        "validations": [
            validate_not_empty,
        ],
    },

        "08_investor_transactions.csv": {

        "expected_columns": [
            "investor_id",
            "transaction_date",
            "amfi_code",
            "transaction_type",
            "amount_inr",
            "state",
            "city",
            "city_tier",
            "age_group",
            "gender",
            "annual_income_lakh",
            "payment_mode",
            "kyc_status",
        ],

        "transformations": [

            standardize_column_names,

            strip_whitespace,

            lambda df: convert_to_datetime(
                df,
                ["transaction_date"],
            ),

            lambda df: convert_numeric_columns(
                df,
                [
                    "amfi_code",
                    "amount_inr",
                    "annual_income_lakh",
                ],
            ),

            remove_duplicate_records,

            lambda df: sort_dataframe(
                df,
                [
                    "transaction_date",
                    "investor_id",
                ],
            ),
        ],

        "validations": [
            validate_not_empty,
        ],
    },

}
DATASET_REGISTRY = [
    {
        "input": filename,
        "output": filename.replace(".csv", "_processed.csv"),
    }
    for filename in DATASET_CONFIG.keys()
]

def get_dataset_config(dataset_name: str) -> dict:
    """
    Return configuration for a dataset.
    """

    if dataset_name not in DATASET_CONFIG:
        raise ValueError(
            f"No configuration found for {dataset_name}"
        )

    return DATASET_CONFIG[dataset_name]