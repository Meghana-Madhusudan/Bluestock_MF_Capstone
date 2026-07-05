import pandas as pd
from pathlib import Path

DATA_PATH = Path("data/raw")

for file in sorted(DATA_PATH.glob("*.csv")):
    print("=" * 80)
    print(file.name)
    print("=" * 80)

    df = pd.read_csv(file)

    print("\nShape")
    print(df.shape)

    print("\nData Types")
    print(df.dtypes)

    print("\nMissing Values")
    print(df.isnull().sum())

    print("\nDuplicate Rows")
    print(df.duplicated().sum())

    print("\nFirst Five Rows")
    print(df.head())

    print("\n")