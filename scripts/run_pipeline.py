from etl.config import (
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    FUND_MASTER_FILE,
    NAV_HISTORY_FILE,
)

from etl.config import (
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    FUND_MASTER_FILE,
    NAV_HISTORY_FILE,
    AUM_BY_FUND_HOUSE_FILE,
)
from etl.pipeline import run_pipeline


def main():

    datasets = [

        {
            "input": FUND_MASTER_FILE,
            "output": "01_fund_master_processed.csv",
        },

        {
            "input": NAV_HISTORY_FILE,
            "output": "02_nav_history_processed.csv",
        },

        {
            "input": AUM_BY_FUND_HOUSE_FILE,
            "output": "03_aum_by_fund_house_processed.csv",
        },

    ]

    for dataset in datasets:

        print("\n" + "=" * 60)
        print(f"Processing: {dataset['input']}")
        print("=" * 60)

        run_pipeline(
            input_path=RAW_DATA_DIR / dataset["input"],
            output_path=PROCESSED_DATA_DIR / dataset["output"],
        )

    print("\n🎉 All datasets processed successfully!")


if __name__ == "__main__":
    main()