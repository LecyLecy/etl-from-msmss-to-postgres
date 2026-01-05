from sqlalchemy import create_engine
import pyodbc
import pandas as pd
import os
import warnings
from sqlalchemy.exc import SAWarning

warnings.filterwarnings(
    "ignore",
    category=SAWarning,
    message=".*Unrecognized server version info.*"
)

# get pass and id MSSMS from environment variables
pwd = os.environ['SqlPass']
id = os.environ['SqlId']

# sql db details
driver = "{ODBC Driver 18 for SQL Server}"
server = os.environ['SSMS_Server']
print(server)
postgres_server = "localhost"
database = "AdventureWorks2022"
pg_db = "AdventureWorks"

def extract():
    try:
        print("Extracting...")
        mssql_engine = create_engine(
            f"mssql+pyodbc://{id}:{pwd}@{server}/{database}"
            "?driver=ODBC+Driver+18+for+SQL+Server"
            "&Encrypt=no"
            "&TrustServerCertificate=yes"
        )

        # Ambil Table yang mau + Supaya Code tau how many to iterate
        query = ("""
                              
                SELECT
                    t.name AS table_name,
                    s.name AS schemas_name
                FROM sys.tables t
                JOIN sys.schemas s
                ON s.schema_id = t.schema_id
                WHERE t.name in ('Department', 'EmailAddress')
                    
                """)
        
        # Take Output to Variable (.fetchall() returns list so we need iteration)
        source_table = pd.read_sql(query, mssql_engine)
        print("Source Table: \n", source_table)

        # for each table we turn to df and load it
        for _, row in source_table.iterrows():
            schema = row["schemas_name"]
            table = row["table_name"]
            df = pd.read_sql_query(f'SELECT * FROM {schema}.{table}', mssql_engine)
            load(df, table)
    except Exception as e:
        print("Error at extract(): ", e)

def load(df, table_name):
    try:
        print("Loading...")
        imported_row = 0
        pg_engine = create_engine(f'postgresql://{id}:{pwd}@{postgres_server}:5432/{pg_db}')
        print(f"Importing On Row {imported_row+1}-{imported_row + len(df)} For Table {table_name}")

        # Loading to Targeted Database
        """
        df.to_sql(
            name, (stg_{table_name})
            con,
            schema=None,
            if_exists='fail',
            index=True, (want index as actual column?, almost always no)
            index_label=None,
            dtype=None,
            method=None,
            chunksize=None
        )
        """
        df.to_sql(f"stg_{table_name}", pg_engine, if_exists='replace', index=False)

        print(f"Successfully Imported Table {table_name}")
    except Exception as e:
        print("Error at load(): ", e)

try:
    print("Starting...")
    extract()
    print("ETL Success!")
except Exception as e:
    print("Error while extract(): ", e)