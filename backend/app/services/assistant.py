from engines.base import BaseEngine


class AssistantService:
    def __init__(self, engine: BaseEngine):
        self.engine = engine

    def generate(self, prompt: str) -> str:
        return self.engine.generate(prompt)
