from fastapi import APIRouter

from app.models.chat import ChatRequest, ChatResponse
from app.services.chat_service import chat

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):

    result = chat(
        telegram_user_id=request.telegram_user_id,
        message=request.message
    )

    return ChatResponse(
        reply=result["reply"]
    )