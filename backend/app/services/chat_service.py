import json

from app.database.user_service import (
    get_user,
    create_user,
)

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

# Watchlist
from app.services.watchlist_service import (
    handle_watchlist_command,
)


# Daily Briefing
from app.services.briefing_ai import (
    is_briefing_request,
)

from app.services.briefing_service import (
    generate_daily_briefing,
)

# Morning Brief
from app.services.morning_ai import (
    detect_morning_intent,
)

from app.services.morning_service import (
    generate_morning_brief,
)

# Evening Wrap
from app.services.evening_ai import (
    detect_evening_intent,
)

from app.services.evening_service import (
    generate_evening_wrap,
)

# Portfolio
from app.services.portfolio_ai import (
    detect_portfolio_intent,
)

from app.services.portfolio_service import (
    generate_portfolio_report,
)

from app.services.onboarding_service import (
    onboarding_required,
    get_next_question,
    process_onboarding,
)
# Comparison

from app.services.comparison_ai import (
    detect_comparison_intent,
)

from app.services.comparison_service import (
    compare_companies,
)

from app.services.finance_service import (
    search_company,
)

def chat(telegram_user_id: int, message: str):

    # --------------------------------------------------
    # Find User
    # --------------------------------------------------

    user = get_user(telegram_user_id)

    # Auto-register new Telegram users
    if not user.data:

        create_user({
            "telegram_user_id": telegram_user_id
        })

        # Fetch newly created user
        user = get_user(telegram_user_id)

    # Get User ID
    user_id = user.data[0]["id"]

    # --------------------------------------------------
    # Load Memory & History
    # --------------------------------------------------

    memory = get_user_memory(user_id)

    history = get_recent_messages(user_id)
    # --------------------------------------------------
    # Onboarding
    # --------------------------------------------------

# --------------------------------------------------
# Onboarding
# --------------------------------------------------

    if onboarding_required(memory):

        if message.lower() in ["hi", "hello", "start"]:

            return {
                "reply": get_next_question(memory)
            }

        reply = process_onboarding(
            user_id,
            memory,
            message
        )

        return {
            "reply": reply
        }

    # ==================================================
    # MORNING BRIEF
    # ==================================================

# ==================================================
# MORNING BRIEF
# ==================================================

    if detect_morning_intent(message):

        report = generate_morning_brief(
            telegram_user_id
        )

        save_message(user_id, "user", message)
        save_message(user_id, "assistant", report)

        return {
            "reply": report
        }


    # ==================================================
    # EVENING MARKET WRAP
    # ==================================================

    if detect_evening_intent(message):

        report = generate_evening_wrap(
            telegram_user_id
        )

        save_message(user_id, "user", message)
        save_message(user_id, "assistant", report)

        return {
            "reply": report
        }


    # ==================================================
    # DAILY BRIEFING
    # ==================================================

    if is_briefing_request(message):

        report = generate_daily_briefing(
            telegram_user_id
        )

        save_message(user_id, "user", message)
        save_message(user_id, "assistant", report)

        return {
            "reply": report
        }
    # ==================================================
    # WATCHLIST
    # ==================================================

    watchlist_reply = handle_watchlist_command(
        user_id,
        message
    )

    if watchlist_reply:

        save_message(user_id, "user", message)
        save_message(user_id, "assistant", watchlist_reply)

        return {
            "reply": watchlist_reply
        }

    # ==================================================
    # PORTFOLIO DASHBOARD
    # ==================================================

    if detect_portfolio_intent(message):

        report = generate_portfolio_report(
            telegram_user_id
        )

        save_message(user_id, "user", message)
        save_message(user_id, "assistant", report)

        return {
            "reply": report
        }
    # ==================================================
# COMPANY COMPARISON
# ==================================================

    if detect_comparison_intent(message):

        # -----------------------------------------
        # Extract comparison companies
        # -----------------------------------------

        comparison_words = [
            " vs ",
            " vs. ",
            " versus ",
            " with ",
            " and ",
        ]

        parts = None

        for word in comparison_words:

            if word in message.lower():

                parts = message.lower().split(word, 1)
                break

        if not parts or len(parts) != 2:

            return {
                "reply": (
                    "📊 To compare companies, try:\n\n"
                    "• Compare Apple vs Microsoft\n"
                    "• Compare Tesla vs Nvidia\n"
                    "• Apple vs Amazon"
                )
            }

        left = parts[0].strip()
        right = parts[1].strip()

        # Remove comparison wording
        for prefix in [
            "compare ",
            "comparison ",
            "compare between ",
        ]:

            if left.startswith(prefix):
                left = left[len(prefix):].strip()

        # -----------------------------------------
        # Resolve companies → tickers
        # -----------------------------------------

        ticker_a = search_company(left)
        ticker_b = search_company(right)

        if not ticker_a or not ticker_b:

            return {
                "reply": (
                    "❌ I couldn't identify both companies.\n\n"
                    "Try something like:\n"
                    "Compare Apple vs Microsoft"
                )
            }

        ticker_a = ticker_a.upper()
        ticker_b = ticker_b.upper()

        if ticker_a == ticker_b:

            return {
                "reply": (
                    "⚠️ Please provide two different companies "
                    "to compare."
                )
            }

        # -----------------------------------------
        # Generate comparison
        # -----------------------------------------

        result = compare_companies([
            ticker_a,
            ticker_b,
        ])

        report = result["report"]

        # -----------------------------------------
        # Save conversation
        # -----------------------------------------

        save_message(
            user_id,
            "user",
            message,
        )

        save_message(
            user_id,
            "assistant",
            report,
        )

        return {
            "reply": report
        }

    # ==================================================
    # NORMAL AI CHAT
    # ==================================================

    answer = generate_response(
        message=message,
        history=history,
        memory=memory,
    )

    # --------------------------------------------------
    # Extract Memory
    # --------------------------------------------------

    extracted = extract_memory(message)

    if extracted.get("role"):

        save_memory(
            user_id,
            "role",
            json.dumps(extracted["role"])
        )

    if extracted.get("briefing_time"):

        save_memory(
            user_id,
            "briefing_time",
            json.dumps(
                extracted["briefing_time"]
            )
        )

    # --------------------------------------------------
    # Save Conversation
    # --------------------------------------------------

    save_message(
        user_id,
        "user",
        message,
    )

    save_message(
        user_id,
        "assistant",
        answer,
    )

    return {
        "reply": answer
    }