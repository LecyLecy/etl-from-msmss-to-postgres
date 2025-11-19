
# ETL: MSSQL to PostgreSQL

This project extracts data from Microsoft SQL Server, processes it using pandas, and loads the final dataset into PostgreSQL using SQLAlchemy.

## 1. Clone the Repository

```bash
git clone https://github.com/USERNAME/REPO-NAME.git
cd REPO-NAME
```

## 2. Create a Virtual Environment

### Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Create a `.env` File

Create a file named `.env` in the project folder and fill in your database credentials:

```
MSSQL_CONN=DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=AdventureWorks2022;UID=sa;PWD=yourpassword
POSTGRES_CONN=postgresql://postgres:yourpassword@localhost:5432/etl_db
```

## 5. Run the ETL Script

```bash
python etl.py
```

## 6. Project Structure

```
ETL_MSSQL_to_Postgres/
│
├── etl.py
├── requirements.txt
├── .gitignore
├── .env
├── README.md
└── venv/
```

## Notes

- The `.env` file is excluded from Git for security reasons.
- The `venv` folder is not included in the repository. Users must create their own virtual environment.
- Ensure that the correct ODBC driver for SQL Server is installed on your system.
