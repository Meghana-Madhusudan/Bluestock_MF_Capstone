# ETL Rules – 03_aum_by_fund_house.csv

## Dataset Overview

This dataset contains Assets Under Management (AUM) information for various mutual fund houses over different reporting dates.

---

## Columns

| Column | Data Type |
|---------|-----------|
| date | Date |
| fund_house | String |
| aum_lakh_crore | Float |
| aum_crore | Integer |
| num_schemes | Integer |

---

# Transformation Rules

## date

- Convert to datetime
- Invalid dates become NaT

---

## fund_house

- Remove leading spaces
- Remove trailing spaces
- Replace multiple spaces with a single space
- Cannot be empty

---

## aum_lakh_crore

- Convert to numeric
- Must be greater than zero

---

## aum_crore

- Convert to numeric
- Must be greater than zero

---

## num_schemes

- Convert to integer
- Must be greater than zero

---

## Duplicate Rows

- Remove duplicate rows.

---

## Sorting

Sort by:

1. date
2. fund_house

---

# Validation Rules

Validate:

- Duplicate rows
- Invalid dates
- Missing fund house
- Invalid aum_lakh_crore
- Invalid aum_crore
- Invalid num_schemes

---

# Output

Processed file:

data/processed/03_aum_by_fund_house_processed.csv

Validation report:

data/reports/03_aum_by_fund_house_validation_report.txt