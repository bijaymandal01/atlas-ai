import json

from app.database.user_service import get_user

from app.database.conversation_service import (
    save_message,
    get_recent_messages,
)

from app.database.memory_service import (
    get_user_memory,
    save_memory,
)

from app.services.gemini_service import generate_response
from app.services.memory_extractor import extract_memory
from app.services.watchlist_service import handle_watchlist_command
from app.services.briefing_ai import is_briefing_request
from app.services.briefing_service import generate_daily_briefing

def chat(telegram_user_id: int, message: str):

    # -----------------------------
    # Find User
    # -----------------------------
    user = get_user(telegram_user_id)

    if not user.data:
        return {
            "reply": "User not found."
        }

    user_id = user.data[0]["id"]

    # -----------------------------
    # Load Memory & History
    # -----------------------------
    memory = get_user_memory(user_id)
    history = get_recent_messages(user_id)

# -----------------------------
# Daily Briefing
# -----------------------------
    if is_briefing_request(message):

        report = generate_daily_briefing(
            telegram_user_id
        )

        save_message(
            user_id,
            "user",
            message
        )

        save_message(
            user_id,
            "assistant",
            report
        )

        return {
            "reply": report
        }

        # -----------------------------
        # Handle Watchlist Commands
        # -----------------------------
        watchlist_reply = handle_watchlist_command(
            user_id,
            message
        )

        if watchlist_reply:

            save_message(
                user_id,
                "user",
                message
            )

            save_message(
                user_id,
                "assistant",
                watchlist_reply
            )

            return {
                "reply": watchlist_reply
            }

    # -----------------------------
    # Generate AI Response
    # -----------------------------
    answer = generate_response(
        message=message,
        history=history,
        memory=memory
    )

    # -----------------------------
    # Extract Memory
    # -----------------------------
    extracted = extract_memory(message)

    # Save Role
    if extracted.get("role"):

        save_memory(
            user_id,
            "role",
            json.dumps(extracted["role"])
        )

    # Save Briefing Time
    if extracted.get("briefing_time"):

        save_memory(
            user_id,
            "briefing_time",
            json.dumps(extracted["briefing_time"])
        )

    # -----------------------------
    # Save Conversation
    # -----------------------------
    save_message(
        user_id,
        "user",
        message
    )

    save_message(
        user_id,
        "assistant",
        answer
    )

    # -----------------------------
    # Return Response
    # -----------------------------
    return {
        "reply": answer
    }