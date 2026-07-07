"""
run_pipeline.py

Execute the ETL pipeline for all configured datasets.
"""

from etl.config import RAW_DATA_DIR, PROCESSED_DATA_DIR
from etl.datasets import DATASET_REGISTRY
from etl.pipeline import run_pipeline


def main():
    """
    Run the ETL pipeline for every dataset registered in DATASET_REGISTRY.
    """

    for dataset in DATASET_REGISTRY:

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