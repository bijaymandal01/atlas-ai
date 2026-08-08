from fastapi import APIRouter

from app.services.chat_service import chat

from app.scheduler.telegram_sender import (
    send_telegram_message,
)

router = APIRouter(
    prefix="/telegram",
    tags=["Telegram"],
)


@router.post("/webhook")
def telegram_webhook(update: dict):

    if "message" not in update:
        return {"ok": True}

    message = update["message"]

    telegram_user_id = message["from"]["id"]

    text = message.get("text", "")

    response = chat(
        telegram_user_id,
        text,
    )

    send_telegram_message(
        telegram_user_id,
        response["reply"],
    )

    return {
        "ok": True
    }