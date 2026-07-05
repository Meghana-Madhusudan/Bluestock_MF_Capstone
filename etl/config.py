from pathlib import Path

# =====================================================
# Project Paths
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"

REPORTS_DIR = BASE_DIR / "data" / "reports"
VALIDATION_REPORTS_DIR = REPORTS_DIR / "validation"

# =====================================================
# Dataset File Names
# =====================================================

FUND_MASTER_FILE = "01_fund_master.csv"
NAV_HISTORY_FILE = "02_nav_history.csv"
AUM_BY_FUND_HOUSE_FILE = "03_aum_by_fund_house.csv"
MONTHLY_SIP_INFLOWS_FILE = "04_monthly_sip_inflows.csv"