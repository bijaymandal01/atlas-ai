import re
import html
import requests

from app.config.settings import TELEGRAM_BOT_TOKEN


MAX_MESSAGE_LENGTH = 4096


# ==================================================
# FORMAT TELEGRAM MESSAGE
# ==================================================

def format_telegram_message(message: str) -> str:
    """
    Convert Atlas AI Markdown-style output into Telegram HTML.
    """

    lines = message.splitlines()

    formatted = []
    table_buffer = []

    def flush_table():

        if not table_buffer:
            return

        table_text = "\n".join(table_buffer)

        formatted.append(
            f"<pre>{html.escape(table_text)}</pre>"
        )

        table_buffer.clear()

    for line in lines:

        stripped = line.strip()

        # -----------------------------------------
        # Markdown table
        # -----------------------------------------

        if stripped.startswith("|") and "|" in stripped:

            table_buffer.append(line)

            continue

        # -----------------------------------------
        # End table
        # -----------------------------------------

        flush_table()

        # -----------------------------------------
        # H1 / H2 / H3 headings
        # -----------------------------------------

        if line.startswith("### "):

            text = line[4:].strip()

            formatted.append(
                f"<b>{html.escape(text)}</b>"
            )

            continue

        if line.startswith("## "):

            text = line[3:].strip()

            formatted.append(
                f"<b>{html.escape(text)}</b>"
            )

            continue

        if line.startswith("# "):

            text = line[2:].strip()

            formatted.append(
                f"<b>{html.escape(text)}</b>"
            )

            continue

        # -----------------------------------------
        # Normal text
        # -----------------------------------------

        escaped = html.escape(line)

        # -----------------------------------------
        # Bold
        # -----------------------------------------

        escaped = re.sub(
            r"\*\*(.*?)\*\*",
            r"<b>\1</b>",
            escaped
        )

        # -----------------------------------------
        # Italic
        # -----------------------------------------

        escaped = re.sub(
            r"(?<!\*)\*(?!\*)(.*?)\*(?!\*)",
            r"<i>\1</i>",
            escaped
        )

        formatted.append(escaped)

    # -----------------------------------------
    # Flush final table
    # -----------------------------------------

    flush_table()

    return "\n".join(formatted)


# ==================================================
# ATLAS AI TELEGRAM MENU
# ==================================================

def get_main_keyboard():
    """
    Return the persistent Atlas AI Telegram menu.
    """

    return {
        "keyboard": [
            [
                {
                    "text": "📊 Portfolio"
                },
                {
                    "text": "⭐ Watchlist"
                },
            ],
            [
                {
                    "text": "🔍 Research Company"
                },
                {
                    "text": "📈 Compare Companies"
                },
            ],
            [
                {
                    "text": "🌅 Morning Brief"
                },
                {
                    "text": "🌆 Evening Wrap"
                },
            ],
            [
                {
                    "text": "📰 Daily Briefing"
                },
            ],
        ],
        "resize_keyboard": True,
        "is_persistent": True,
        "input_field_placeholder": "Ask Atlas anything..."
    }


# ==================================================
# NORMAL TELEGRAM MESSAGE
# ==================================================

def send_telegram_message(
    chat_id: int,
    message: str
):
    """
    Send an Atlas AI message to Telegram.

    Converts Markdown-style AI output into
    Telegram HTML formatting.

    Automatically splits long messages.

    The Atlas AI menu is attached to every message.
    """

    url = (
        f"https://api.telegram.org/bot"
        f"{TELEGRAM_BOT_TOKEN}/sendMessage"
    )

    formatted_message = format_telegram_message(
        message
    )

    keyboard = get_main_keyboard()

    for i in range(
        0,
        len(formatted_message),
        MAX_MESSAGE_LENGTH
    ):

        chunk = formatted_message[
            i:i + MAX_MESSAGE_LENGTH
        ]

        payload = {
            "chat_id": chat_id,
            "text": chunk,
            "parse_mode": "HTML",
            "reply_markup": keyboard,
        }

        response = requests.post(
            url,
            json=payload,
            timeout=30,
        )

        response.raise_for_status()

    return True