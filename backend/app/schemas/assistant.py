from pydantic import BaseModel


class PromptRequest(BaseModel):
    content: str


class PromptResponse(BaseModel):
    content: str
