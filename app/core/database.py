from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = URL.create(
    "postgresql+psycopg2",
    username="postgres",
    password="REDsiren@911",
    host="localhost",
    port=5432,
    database="SatTrack"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()