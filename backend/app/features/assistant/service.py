from features.assistant.engines.base import BaseEngine


class AssistantService:
    def __init__(self, engine: BaseEngine):
        self.engine = engine

    def generate(self, prompt: str) -> str:
        content = self.engine.generate(prompt)

        return content
