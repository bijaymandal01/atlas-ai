from app.database.user_service import get_user
from app.database.watchlist_service import get_watchlist

from app.services.briefing_builder import (
    build_briefing_dashboard,
)

from app.services.briefing_prompt import (
    build_briefing_prompt,
)

from app.services.gemini_service import (
    generate_research,
)


def generate_daily_briefing(telegram_user_id: int):
    """
    Generate a personalized daily financial briefing.
    """

    # ---------------------------------
    # Get User
    # ---------------------------------
    user = get_user(telegram_user_id)

    if not user.data:
        return "❌ User not found."

    user_id = user.data[0]["id"]

    # ---------------------------------
    # Get Watchlist
    # ---------------------------------
    watchlist = get_watchlist(user_id)

    if not watchlist.data:
        return "📊 Your watchlist is empty."

    # ---------------------------------
    # Build Dashboard
    # ---------------------------------
    dashboard = build_briefing_dashboard(
        watchlist
    )

    # ---------------------------------
    # Build Gemini Prompt
    # ---------------------------------
    prompt = build_briefing_prompt(
        dashboard
    )

    # ---------------------------------
    # AI Analysis
    # ---------------------------------
    analysis = generate_research(
        prompt
    )

    # ---------------------------------
    # Final Report
    # ---------------------------------
    report = f"""
{dashboard}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🤖 ATLAS AI INSIGHT

{analysis}
"""

    return report