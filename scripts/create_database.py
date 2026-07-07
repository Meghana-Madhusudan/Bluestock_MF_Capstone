import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

DB_PATH = BASE_DIR / "database" / "mutual_fund.db"

SCHEMA_PATH = BASE_DIR / "database" / "schema.sql"


def create_database():

    DB_PATH.parent.mkdir(exist_ok=True)

    conn = sqlite3.connect(DB_PATH)

    with open(SCHEMA_PATH, "r") as file:
        schema = file.read()

    conn.executescript(schema)

    conn.close()

    print("Database created successfully")
    print(DB_PATH)


if __name__ == "__main__":
    create_database()