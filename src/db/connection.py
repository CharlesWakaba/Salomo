from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.config.settings import settings

engine = create_engine(settings.DATABASE_URL)
Session = sessionmaker(bind=engine)

def get_db_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()
