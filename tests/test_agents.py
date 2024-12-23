import pytest
from src.agents.database_agent import DatabaseAgent
from src.agents.africas_talking_agent import AfricasTalkingAgent

@pytest.fixture
def db_agent():
    return DatabaseAgent()

@pytest.fixture
def at_agent():
    class MockAfricasTalkingAgent(AfricasTalkingAgent):
        def generate_response(self, query):
            return {'mocked': 'response'}
    
    return MockAfricasTalkingAgent()

def test_database_agent(db_agent):
    result = db_agent.generate_response('test query')
    assert result is not None

def test_africas_talking_agent(at_agent):
    result = at_agent.generate_response('test query')
    assert result == {'mocked': 'response'}
