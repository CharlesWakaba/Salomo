import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///rag_system.db')
    AFRICAS_TALKING_API_KEY = os.getenv('AFRICAS_TALKING_API_KEY')

settings = Settings()
