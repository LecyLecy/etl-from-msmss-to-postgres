from sqlalchemy import create_engine
import pyodbc
import pandas as pd
import os

pwd = os.getenv("SqlPass")
id = os.getenv("SqlId")