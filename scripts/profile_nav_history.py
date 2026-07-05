import pandas as pd
from pathlib import Path

# -----------------------------
# File Path
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "raw" / "02_nav_history.csv"

# -----------------------------
# Load Dataset
# -----------------------------
try:
    df = pd.read_csv(DATA_PATH)
    print("✅ Dataset loaded successfully.\n")
except FileNotFoundError:
    print("❌ File not found.")
    exit()

# -----------------------------
# Dataset Shape
# -----------------------------
print("=" * 60)
print("DATASET SHAPE")
print("=" * 60)
print(f"Rows    : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")

print(f"Unique AMFI Codes : {df['amfi_code'].nunique()}")
print(f"Unique Dates : {df['date'].nunique()}")

# -----------------------------
# Column Names
# -----------------------------
print("\n" + "=" * 60)
print("COLUMN NAMES")
print("=" * 60)

for col in df.columns:
    print(f"- {col}")

# -----------------------------
# Data Types
# -----------------------------
print("\n" + "=" * 60)
print("DATA TYPES")
print("=" * 60)

print(df.dtypes)

# -----------------------------
# Missing Values
# -----------------------------
print("\n" + "=" * 60)
print("MISSING VALUES")
print("=" * 60)

missing = df.isnull().sum()

missing_df = pd.DataFrame({
    "Column": missing.index,
    "Missing Values": missing.values,
    "Missing %": ((missing.values / len(df)) * 100).round(2)
})

print(missing_df)

# -----------------------------
# Duplicate Rows
# -----------------------------
print("\n" + "=" * 60)
print("DUPLICATE ROWS")
print("=" * 60)

duplicates = df.duplicated().sum()

print(f"Total Duplicate Rows : {duplicates}")

# -----------------------------
# Summary Statistics
# -----------------------------
print("\n" + "=" * 60)
print("SUMMARY STATISTICS")
print("=" * 60)

print(df.describe(include="all"))

# -----------------------------
# Date Range
# -----------------------------
print("\n" + "=" * 60)
print("DATE RANGE")
print("=" * 60)

print(f"Earliest Date : {df['date'].min()}")
print(f"Latest Date   : {df['date'].max()}")

# -----------------------------
# First 5 Rows
# -----------------------------
print("\n" + "=" * 60)
print("FIRST 5 ROWS")
print("=" * 60)

print(df.head())

# -----------------------------
# Last 5 Rows
# -----------------------------
print("\n" + "=" * 60)
print("LAST 5 ROWS")
print("=" * 60)

print(df.tail())

print("\n✅ Data profiling completed successfully.")