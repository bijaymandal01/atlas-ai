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

    # --------------------------------------------------
    # Ignore updates that don't contain a message
    # --------------------------------------------------

    if "message" not in update:
        return {
            "ok": True
        }

    message = update["message"]

    telegram_user_id = message["from"]["id"]

    text = message.get(
        "text",
        ""
    )

    # --------------------------------------------------
    # Atlas AI Chat
    # --------------------------------------------------

    response = chat(
        telegram_user_id,
        text,
    )

    # --------------------------------------------------
    # Send Atlas Response
    # Telegram sender automatically attaches
    # the persistent menu to the message.
    # --------------------------------------------------

    send_telegram_message(
        telegram_user_id,
        response["reply"],
    )

    return {
        "ok": True
    }