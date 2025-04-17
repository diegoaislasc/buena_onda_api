# connect and log into a PostgreSQL database
# https://www.pg4e.com/lectures/06-Python.php

import psycopg2
from dotenv import load_dotenv
import os
from pathlib import Path
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")

# retrieve .env data
host = os.getenv("PG_HOST")
dbname = os.getenv("PG_DB")
user = os.getenv("PG_USER")
password = os.getenv("PG_PASS")


Base = declarative_base()
engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}/{dbname}')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

print("Conexión exitosa")



