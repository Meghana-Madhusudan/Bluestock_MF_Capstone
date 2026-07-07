"""
load_database.py

Loads processed ETL datasets into SQLite database.
"""

from pathlib import Path
import sqlite3
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent

PROCESSED_DIR = BASE_DIR / "data" / "processed"

DB_PATH = BASE_DIR / "database" / "mutual_fund.db"


DATASET_TABLE_MAP = {

    "01_fund_master_processed.csv": "fund_master",

    "02_nav_history_processed.csv": "nav_history",

    "03_aum_by_fund_house_processed.csv": "aum_by_fund_house",

    "04_monthly_sip_inflows_processed.csv": "monthly_sip_inflows",

    "05_category_inflows_processed.csv": "category_inflows",

    "06_industry_folio_count_processed.csv": "industry_folio_count",

    "07_scheme_performance_processed.csv": "scheme_performance",

    "08_investor_transactions_processed.csv": "investor_transactions",

    "09_portfolio_holdings_processed.csv": "portfolio_holdings",

    "10_benchmark_indices_processed.csv": "benchmark_indices"
}


def load_dataset(file_name, table_name, connection):

    file_path = PROCESSED_DIR / file_name

    if not file_path.exists():

        print(f"❌ Missing file: {file_name}")
        return


    print("\nLoading:", file_name)


    df = pd.read_csv(file_path)


    df.to_sql(
        table_name,
        connection,
        if_exists="replace",
        index=False
    )


    print(
        f"✅ Loaded {len(df)} rows into {table_name}"
    )



def load_database():

    print("="*60)
    print("Loading Processed Datasets into SQLite")
    print("="*60)


    connection = sqlite3.connect(DB_PATH)


    try:

        for file_name, table_name in DATASET_TABLE_MAP.items():

            load_dataset(
                file_name,
                table_name,
                connection
            )


        connection.commit()


    finally:

        connection.close()


    print("\nDatabase loading completed successfully")



if __name__ == "__main__":
    load_database()