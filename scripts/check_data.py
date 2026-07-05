import pandas as pd
from pathlib import Path

# Path to raw data folder
DATA_PATH = Path("data/raw")

# List all CSV files
csv_files = sorted(DATA_PATH.glob("*.csv"))

print("=" * 80)
print("BLUESTOCK MUTUAL FUND CAPSTONE")
print("=" * 80)

for file in csv_files:
    df = pd.read_csv(file)

    print(f"\nDataset: {file.name}")
    print("-" * 60)
    print(f"Rows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")
    print("\nColumn Names:")
    print(list(df.columns))