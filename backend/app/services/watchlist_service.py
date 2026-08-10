from app.services.watchlist_ai import detect_watchlist_intent
from app.database.watchlist_service import (
    add_company,
    remove_company,
    get_watchlist,
    company_exists,
)

from app.services.finance_service import search_company
def handle_watchlist_command(user_id: str, message: str):
    """
    Handle natural language watchlist commands.

    Returns:
        str -> reply if command handled
        None -> if message is not a watchlist command
    """

    intent = detect_watchlist_intent(message)

    if not intent:
        return None

    # ==========================================
    # ADD COMPANY
    # ==========================================
    if intent["intent"] == "add":

        company = intent["company"].strip().title()

        ticker = search_company(company)

        if not ticker:
            return (
                f"❌ I couldn't find a valid stock "
                f"ticker for {company}."
            )

        exists = company_exists(
            user_id,
            company
        )

        if exists.data:
            return (
                f"📊 {company} is already in your watchlist."
            )

        add_company({
            "user_id": user_id,
            "company_name": company,
            "ticker": ticker
        })

        watchlist = get_watchlist(user_id)

        companies = [
            item["company_name"]
            for item in watchlist.data
        ]

        reply = (
            f"✅ {company} ({ticker}) added "
            f"to your watchlist.\n\n"
        )

        reply += (
            f"📊 Current Watchlist "
            f"({len(companies)})\n\n"
        )

        for item in watchlist.data:
            reply += (
                f"• {item['company_name']} "
                f"({item['ticker']})\n"
            )

        return reply.strip()
        # ==========================================
        # REMOVE COMPANY
        # ==========================================
        if intent["intent"] == "remove":

            company = intent["company"].title()

            exists = company_exists(user_id, company)

            if not exists.data:
                return f"📊 {company} is not in your watchlist."

            remove_company(user_id, company)

            watchlist = get_watchlist(user_id)

            companies = [
                item["company_name"]
                for item in watchlist.data
            ]

            reply = f"🗑️ {company} removed from your watchlist.\n\n"

            if companies:

                reply += f"📊 Current Watchlist ({len(companies)})\n\n"

                for c in companies:
                    reply += f"• {c}\n"

            else:
                reply += "📊 Your watchlist is empty."

            return reply.strip()

    # ==========================================
    # SHOW WATCHLIST
    # ==========================================
    if intent["intent"] == "show":

        watchlist = get_watchlist(user_id)

        companies = [
            item["company_name"]
            for item in watchlist.data
        ]

        if not companies:
            return "📊 Your watchlist is empty."

        reply = f"📊 Current Watchlist ({len(companies)})\n\n"

        for c in companies:
            reply += f"• {c}\n"

        return reply.strip()

    return None



def add_watchlist_from_onboarding(
    user_id: str,
    companies: list[str],
):
    """
    Add multiple companies during onboarding.
    """

    for company in companies:

        company = company.strip().title()

        if not company:
            continue

        ticker = search_company(company)

        if not ticker:
            continue

        exists = company_exists(
            user_id,
            company
        )

        if exists.data:
            continue

        add_company({
            "user_id": user_id,
            "company_name": company,
            "ticker": ticker
        })