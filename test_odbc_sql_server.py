import pyodbc
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

# def load_database() :
id = os.getenv("SqlId")
pwd = os.getenv("SqlPass")
driver = os.getenv("SqlDriver")
server = os.getenv("SqlServer")
database_source = os.getenv("SqlSource")

conn_str = (
    f"DRIVER={driver};" 
    f"SERVER={server};" 
    f"DATABASE={database_source};" 
    f"UID={id};" 
    f"PWD={pwd};"
)

print(conn_str)

conn = pyodbc.connect(conn_str)

# def sql_query() :
sql_query = 'SELECT * FROM Production.Culture'

df = pd.read_sql_query(sql_query, conn)
df.head()