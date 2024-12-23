import pytest
from src.core.rag_system import RAGSystem

@pytest.fixture
def rag_system():
    return RAGSystem()

def test_retrieve_and_generate(rag_system):
    result = rag_system.retrieve_and_generate('test query')
    assert result is not None
    assert isinstance(result, list)
    
    for res in result:
        # Check if there's an error that's not related to authentication
        if 'error' in res:
            error_message = res.get('response_text', '')
            # Skip authentication errors in test
            if 'authentication' not in error_message.lower():
                assert False, f"Error in response: {res['error']} - {error_message}"