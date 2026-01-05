# MSSQL to PostgreSQL ETL Pipeline

This project implements an end-to-end ETL (Extract, Transform, Load) pipeline that transfers data from **Microsoft SQL Server (SSMS)** to **PostgreSQL** using **Python**, **SQLAlchemy**, **pyodbc**, and **pandas**.

The pipeline is designed with real-world ETL practices in mind, including schema handling, type casting, and staging tables.

---

## Tech Stack

- Python 3.10
- pandas
- SQLAlchemy
- pyodbc
- psycopg2
- Microsoft SQL Server (AdventureWorks2022)
- PostgreSQL

---

## Project Structure

```
ETL_MSMSS_To_Postgres/
│
├── etl.py                    # Main ETL script
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
├── .gitignore                # Ignored files & folders
├── .env                      # Environment variables (ignored)
├── venv310/                  # Python virtual environment (ignored)
└── test_odbc_sql_server.py   # Connection testing script
```

---

## Environment Variables

Create a `.env` file (not committed to git):

```env
SqlId=etl
SqlPass=your_password
SSMS_Server=your_ssms_server
```

---

## ETL Flow

### Extract

- Connects to SQL Server using SQLAlchemy + pyodbc
- Reads table metadata from `sys.tables` and `sys.schemas`
- Explicitly selects columns (avoids `SELECT *`)
- Casts unsupported types (e.g. `datetimeoffset → datetime2`)

### Load

- Connects to PostgreSQL using SQLAlchemy + psycopg2
- Loads data into staging tables (`stg_<table_name>`)
- Uses `if_exists="replace"` for idempotent loads

---

## How to Run

```bash
venv310\Scripts\activate
pip install -r requirements.txt
python etl.py
```

---

## Notes

- `SELECT *` is intentionally avoided for cross-database compatibility
- PostgreSQL permissions must allow `CREATE` on target schema
- Designed for extensibility (incremental loads, upserts, schema separation)

---

## Status

✅ Completed
This project represents a production-style ETL pipeline suitable for learning, coursework, and portfolio use.
