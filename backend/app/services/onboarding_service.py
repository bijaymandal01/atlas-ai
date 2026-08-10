import json

from app.database.memory_service import save_memory
from app.services.watchlist_service import (
    add_watchlist_from_onboarding,
)

ONBOARDING_STEPS = [
    "role",
    "market",
    "watchlist",
    "briefing_time",
]

QUESTIONS = {
    "role": (
        "👋 Welcome to Atlas AI!\n\n"
        "Before we begin, I'd like to personalize your experience.\n\n"
        "Which best describes you?\n\n"
        "1️⃣ Investor\n"
        "2️⃣ Student\n"
        "3️⃣ Trader\n"
        "4️⃣ Finance Professional\n"
        "5️⃣ Business Owner\n"
        "6️⃣ Other"
    ),

    "market": (
        "🌍 Which market do you mainly follow?\n\n"
        "🇺🇸 US Stocks\n"
        "🇮🇳 Indian Stocks\n"
        "₿ Crypto\n"
        "📈 ETFs\n"
        "🌎 Global"
    ),

    "watchlist": (
        "📈 Which companies would you like Atlas AI to track?\n\n"
        "Example:\n"
        "Apple\n"
        "Microsoft\n"
        "Tesla"
    ),

    "briefing_time": (
        "⏰ What time would you like to receive your Morning Brief?\n\n"
        "Example:\n"
        "8:00 AM"
    ),
}
def memory_to_dict(memory):

    result = {}

    for item in memory:
        result[item["memory_key"]] = item["memory_value"]

    return result


def get_next_step(memory):

    memory = memory_to_dict(memory)

    for step in ONBOARDING_STEPS:

        if step not in memory:
            return step

    return None


def onboarding_required(memory):

    return get_next_step(memory) is not None


def get_next_question(memory):

    step = get_next_step(memory)

    if step is None:
        return None

    return QUESTIONS[step]

def process_onboarding(user_id, memory, message):

    step = get_next_step(memory)

    if step is None:
        return None

    # -----------------------
    # ROLE
    # -----------------------

    if step == "role":

        role = message.strip().title()

        save_memory(
            user_id,
            "role",
            json.dumps(role)
        )

        return QUESTIONS["market"]

    # -----------------------
    # MARKET
    # -----------------------

    if step == "market":

        market = message.strip().title()

        save_memory(
            user_id,
            "market",
            json.dumps(market)
        )

        return QUESTIONS["watchlist"]

    # -----------------------
    # WATCHLIST
    # -----------------------

    if step == "watchlist":

        companies = [
            company.strip()
            for company in message.split(",")
            if company.strip()
        ]

        add_watchlist_from_onboarding(
            user_id,
            companies
        )

        save_memory(
            user_id,
            "watchlist",
            json.dumps(companies)
        )

        return QUESTIONS["briefing_time"]

    # -----------------------
    # BRIEFING TIME
    # -----------------------

    if step == "briefing_time":

        briefing_time = message.strip()

        save_memory(
            user_id,
            "briefing_time",
            json.dumps(briefing_time)
        )

        return (
            "🎉 Atlas AI is ready!\n\n"
            "Your profile has been created successfully.\n\n"
            "You can now:\n"
            "• Chat with Atlas AI\n"
            "• Manage your watchlist\n"
            "• Generate Morning Briefs\n"
            "• Generate Evening Wraps\n"
            "• Research companies\n"
            "• Compare stocks"
        )

    return None