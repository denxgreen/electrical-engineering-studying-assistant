from sqlalchemy.orm import Session

from engines.base import BaseEngine


class AssistantService:
    def __init__(self, engine: BaseEngine, session: Session):
        self.engine = engine
        self._session = session

    def generate(self, prompt: str) -> str:
        content = self.engine.generate(prompt)

        return content
