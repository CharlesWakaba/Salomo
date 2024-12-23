import requests
from src.agents.base import BaseAgent
from src.config.settings import settings

class AfricasTalkingAgent(BaseAgent):
    def __init__(self):
        super().__init__('AfricasTalkingAgent')
        self.api_key = settings.AFRICAS_TALKING_API_KEY
        # Updated API URL to use the sandbox environment
        self.api_url = 'https://api.sandbox.africastalking.com/version1/messaging'
    
    def generate_response(self, query):
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded',
            'apiKey': self.api_key
        }
        
        payload = {
            'username': 'sandbox',
            'to': '+254711XXXYYY',  
            'message': f'Query: {query}'
        }

        try:
            response = requests.post(
                self.api_url, 
                headers=headers, 
                data=payload
            )
            response.raise_for_status()  
            return response.json()
        except requests.exceptions.RequestException as e:
            return {
                'error': str(e),
                'status_code': getattr(response, 'status_code', None),
                'response_text': getattr(response, 'text', str(e))
            }