from abc import ABC, abstractmethod

class BaseEngine(ABC):
    '''
        Base class for AI Engine such as OpenAI, Gemini, etc.
    '''
    
    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass
