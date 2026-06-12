#db module for SQLAlchemy setup and database connection management
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv() #.env -> systems env variable 

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set. Copy .env.example to .env and fill in your credentials.")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker( #session factory for creating database sessions
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base() #base class for all database models, the class all the my models will inherit from

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()