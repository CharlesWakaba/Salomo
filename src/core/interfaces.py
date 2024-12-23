from abc import ABC, abstractmethod

class AIModelInterface(ABC):
    @abstractmethod
    def generate_response(self, query):
        pass
