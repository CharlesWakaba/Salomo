from src.core.interfaces import AIModelInterface

class BaseAgent(AIModelInterface):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
