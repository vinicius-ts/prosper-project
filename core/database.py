from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLACHEMY_DATABASE_URL = "postgresql://root:root@prosper_db:5432/prosperdb"

engine = create_engine(SQLACHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


