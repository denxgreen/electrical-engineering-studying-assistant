from groq import Groq

from engines.base import BaseEngine

class GroqEngine(BaseEngine):
    '''
    Parameters
    ----------
    api_key : str
    model: str
    system_prompt: str
    '''

    def __init__(self, api_key: str, model: str, system_prompt: str):
        self.api_key = api_key
        self.model = model
        self.system_prompt = system_prompt
        self.client = Groq(api_key=self.api_key)

    def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    'role': 'system',
                    'content': self.system_prompt,
                },
                {
                    'role': 'user',
                    'content': prompt,
                }
            ]
        )

        return response.choices[0].message.content
