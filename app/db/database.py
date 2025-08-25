from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

USERNAME = "postgres"
PASSWORD = "8910"
HOST = "localhost"
PORT = 5432
NAME = "wallet"

DATABASE_URL = (f"postgresql://{USERNAME}:{PASSWORD}"
                f"@{HOST}:{PORT}/{NAME}")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()

Base.metadata.create_all(bind=engine)

@contextmanager
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

