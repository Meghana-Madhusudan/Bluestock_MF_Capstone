CREATE TABLE IF NOT EXISTS fund_master (
    fund_id INTEGER PRIMARY KEY,
    fund_name TEXT,
    fund_house TEXT,
    category TEXT,
    launch_date TEXT
);


CREATE TABLE IF NOT EXISTS nav_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fund_id INTEGER,
    nav_date TEXT,
    nav_value REAL
);


CREATE TABLE IF NOT EXISTS aum_by_fund_house (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fund_house TEXT,
    year INTEGER,
    aum REAL
);


CREATE TABLE IF NOT EXISTS monthly_sip_inflows (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    month TEXT,
    category TEXT,
    sip_amount REAL
);


CREATE TABLE IF NOT EXISTS category_inflows (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    month TEXT,
    category TEXT,
    inflow REAL
);


CREATE TABLE IF NOT EXISTS industry_folio_count (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    industry TEXT,
    folio_count INTEGER
);


CREATE TABLE IF NOT EXISTS scheme_performance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fund_id INTEGER,
    return_1y REAL,
    return_3y REAL,
    return_5y REAL
);


CREATE TABLE IF NOT EXISTS investor_transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    investor_id TEXT,
    fund_id INTEGER,
    transaction_type TEXT,
    amount REAL,
    transaction_date TEXT
);


CREATE TABLE IF NOT EXISTS portfolio_holdings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fund_id INTEGER,
    stock_name TEXT,
    sector TEXT,
    allocation REAL
);


CREATE TABLE IF NOT EXISTS benchmark_indices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    index_name TEXT,
    date TEXT,
    close_value REAL
);
