from datetime import datetime

from app.database.user_service import get_user
from app.database.watchlist_service import get_watchlist

from app.services.morning_builder import (
    build_morning_data,
)

from app.services.morning_prompt import (
    build_morning_prompt,
)

from app.services.gemini_service import (
    generate_research,
)


def generate_morning_brief(telegram_user_id: int):
    """
    Generate Atlas AI Morning Brief.
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
    # Collect Data
    # ---------------------------------
    companies = build_morning_data(watchlist)

    # ---------------------------------
    # Generate AI Insight
    # ---------------------------------
    prompt = build_morning_prompt(companies)

    insight = generate_research(prompt)

    # ---------------------------------
    # Build Dashboard
    # ---------------------------------
    today = datetime.now().strftime("%A, %d %b %Y")

    report = f"""🌅 ATLAS AI MORNING BRIEF

📅 {today}
⏰ Before Market Open

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 YOUR WATCHLIST
"""

    # -----------------------------
    # Watchlist
    # -----------------------------
    for company in companies:

        price = company["price"]
        performance = company["performance"]
        news = company["news"]

        report += f"""

━━━━━━━━━━━━━━━━━━━━━━

🏢 {company["company"]} ({company["ticker"]})

💲 Price        ${price.get("current_price", "N/A")}
📈 Yesterday    {performance.get("today", "N/A")}%
📅 This Week    {performance.get("week", "N/A")}%
📆 This Month   {performance.get("month", "N/A")}%
🗓️ This Year    {performance.get("year", "N/A")}%

📰 Top Headline
"""

        if news:
            report += f"{news[0]['title']}\n"
        else:
            report += "No major news.\n"

    # -----------------------------
    # Market Headlines
    # -----------------------------
    report += """

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📰 MARKET HEADLINES

"""

    shown = set()

    for company in companies:
        for article in company["news"][:1]:

            title = article["title"]

            if title not in shown:
                shown.add(title)
                report += f"• {title}\n"

    # -----------------------------
    # Today's Focus
    # -----------------------------
    report += """

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📅 TODAY'S FOCUS

"""

    for company in companies:

        report += f"""• {company["company"]}

"""

    # -----------------------------
    # AI Insight
    # -----------------------------
    report += """

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🤖 ATLAS AI INSIGHT

"""

    report += insight

    report += """

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🚀 Have a productive trading day!
"""

    return report