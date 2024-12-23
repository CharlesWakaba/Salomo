from src.agents.base import BaseAgent
from src.db.connection import get_db_session
from src.db.setup import Data

class DatabaseAgent(BaseAgent):
    def __init__(self):
        super().__init__('DatabaseAgent')

    def generate_response(self, query):
        session = next(get_db_session())
        result = session.query(Data).filter(Data.content.contains(query)).all()
        return result
