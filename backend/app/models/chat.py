from pydantic import BaseModel


class ChatRequest(BaseModel):
    telegram_user_id: int
    message: str


class ChatResponse(BaseModel):
    reply: str