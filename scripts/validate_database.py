"""
validate_database.py

Validates SQLite database integrity
after loading processed datasets.
"""

from pathlib import Path
import sqlite3


BASE_DIR = Path(__file__).resolve().parent.parent

DB_PATH = BASE_DIR / "database" / "mutual_fund.db"


TABLES = [
    "fund_master",
    "nav_history",
    "aum_by_fund_house",
    "monthly_sip_inflows",
    "category_inflows",
    "industry_folio_count",
    "scheme_performance",
    "investor_transactions",
    "portfolio_holdings",
    "benchmark_indices"
]


def validate_database():

    print("="*60)
    print("DATABASE VALIDATION")
    print("="*60)


    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()


    print("\nChecking tables...\n")


    for table in TABLES:

        cursor.execute(
            f"SELECT COUNT(*) FROM {table}"
        )

        count = cursor.fetchone()[0]


        if count > 0:

            print(
                f"✅ {table}: {count} rows"
            )

        else:

            print(
                f"❌ {table}: EMPTY"
            )


    print("\nRunning sample queries...\n")


    # Top funds
    cursor.execute(
        """
        SELECT *
        FROM fund_master
        LIMIT 5
        """
    )


    print("Sample fund_master records:")

    for row in cursor.fetchall():

        print(row)



    # NAV check

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM nav_history
        """
    )


    nav_count = cursor.fetchone()[0]


    print(
        f"\nNAV Records: {nav_count}"
    )


    conn.close()


    print("\nDatabase validation completed.")



if __name__ == "__main__":

    validate_database()