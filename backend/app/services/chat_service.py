import json

from app.database.user_service import get_user

from app.database.conversation_service import (
    save_message,
    get_recent_messages
)

from app.database.memory_service import (
    get_user_memory,
    get_memory_by_key,
    save_memory
)

from app.services.gemini_service import generate_response
from app.services.memory_extractor import extract_memory


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

    watchlist_updated = False
    current_watchlist = []
    newly_added = []

    # -----------------------------
    # Save Role
    # -----------------------------
    if extracted.get("role"):

        save_memory(
            user_id,
            "role",
            json.dumps(extracted["role"])
        )

    # -----------------------------
    # Save Briefing Time
    # -----------------------------
    if extracted.get("briefing_time"):

        save_memory(
            user_id,
            "briefing_time",
            json.dumps(extracted["briefing_time"])
        )

    # -----------------------------
    # Merge Companies
    # -----------------------------
    companies = extracted.get("companies_to_add", [])

    if companies:

        existing = get_memory_by_key(
            user_id,
            "companies"
        )

        old_companies = []

        if existing:

            old_companies = existing["memory_value"]

            if not isinstance(old_companies, list):
                old_companies = []

        # Find only new companies
        for company in companies:
            if company not in old_companies:
                newly_added.append(company)

        merged = list(
            dict.fromkeys(
                old_companies + companies
            )
        )

        current_watchlist = merged

        save_memory(
            user_id,
            "companies",
            json.dumps(merged)
        )

        if newly_added:
            watchlist_updated = True

    else:

        existing = get_memory_by_key(
            user_id,
            "companies"
        )

        if existing:
            current_watchlist = existing["memory_value"]

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
        message=answer
    )

    # -----------------------------
    # Build Final Response
    # -----------------------------
    if watchlist_updated:

        answer += "\n\n━━━━━━━━━━━━━━━━━━━━━━"
        answer += "\n✅ Watchlist Updated"

        answer += "\n\n🆕 Added"

        for company in newly_added:
            answer += f"\n• {company}"

        answer += f"\n\n📊 Current Watchlist ({len(current_watchlist)})"

        for company in current_watchlist:
            answer += f"\n• {company}"

        answer += "\n━━━━━━━━━━━━━━━━━━━━━━"

    return {
        "reply": answer
    }