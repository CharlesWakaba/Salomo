from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from src.config.settings import settings
from sqlalchemy.orm import declarative_base

Base = declarative_base()

Base = declarative_base()
engine = create_engine(settings.DATABASE_URL)

class Data(Base):
    __tablename__ = 'data'
    id = Column(Integer, primary_key=True)
    content = Column(Text)

def setup_database():
    Base.metadata.create_all(engine)
