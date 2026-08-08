import requests

from app.config.settings import TELEGRAM_BOT_TOKEN

MAX_MESSAGE_LENGTH = 4096


def send_telegram_message(chat_id: int, message: str):
    """
    Send a Telegram message.
    Automatically splits long messages.
    """

    url = (
        f"https://api.telegram.org/bot"
        f"{TELEGRAM_BOT_TOKEN}/sendMessage"
    )

    for i in range(0, len(message), MAX_MESSAGE_LENGTH):

        chunk = message[i:i + MAX_MESSAGE_LENGTH]

        payload = {
            "chat_id": chat_id,
            "text": chunk,
        }

        response = requests.post(
            url,
            json=payload,
            timeout=30,
        )

        response.raise_for_status()

    return True