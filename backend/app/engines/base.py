from abc import ABC, abstractmethod

class BaseEngine(ABC):
    '''
        Base class for AI Engine such as OpenAI, Gemini, etc.
    '''

    def __init__(self, api_key: str, model: str, system_prompt: str):
        self.api_key = api_key
        self.model = model
        self.system_prompt = system_prompt

    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass
