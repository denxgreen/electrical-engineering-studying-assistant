from pydantic import BaseModel, ConfigDict, Field


class PromptBase(BaseModel):
    content: str = Field(min_length=1, max_length=10000)


class PromptRequest(PromptBase):
    model_config = ConfigDict(from_attributes=True)
        

class PromptResponse(PromptBase):
    model_config = ConfigDict(from_attributes=True)
