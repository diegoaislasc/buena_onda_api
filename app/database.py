# connect and log into a PostgreSQL database
# https://www.pg4e.com/lectures/06-Python.php
import psycopg2
from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")

# retrieve .env data
host = os.getenv("PG_HOST")
dbname = os.getenv("PG_DB")
user = os.getenv("PG_USER")
password = os.getenv("PG_PASS")

print("HOST:", host)
print("DB:", dbname)
print("USER:", user)
print("PASS:", password)

# pg connection
conn = psycopg2.connect(
    host=host,
    database=dbname,
    user=user,
    password=password,
    connect_timeout=3
)

print("Conexión exitosa")



