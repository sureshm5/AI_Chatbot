from pydantic import BaseModel


class ConversationCreate(BaseModel):
    pass


class ConversationResponse(BaseModel):
    id: int
    title: str
    model_used: str
    provider: str

    class Config:
        from_attributes = True