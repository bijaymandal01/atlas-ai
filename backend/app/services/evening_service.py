from datetime import datetime

from app.database.user_service import get_user
from app.database.watchlist_service import get_watchlist

from app.services.evening_builder import (
    build_evening_data,
)

from app.services.evening_prompt import (
    build_evening_prompt,
)

from app.services.gemini_service import (
    generate_research,
)


def generate_evening_wrap(telegram_user_id: int):
    """
    Generate Atlas AI Evening Market Wrap.
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
    companies = build_evening_data(watchlist)

    # ---------------------------------
    # AI Insight
    # ---------------------------------
    prompt = build_evening_prompt(companies)

    insight = generate_research(prompt)

    # ---------------------------------
    # Build Dashboard
    # ---------------------------------
    today = datetime.now().strftime("%A, %d %b %Y")

    report = f"""🌆 ATLAS AI MARKET WRAP

📅 {today}
⏰ After Market Close

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 TODAY'S WATCHLIST
"""

    best = None
    worst = None

    headlines = set()

    # ---------------------------------
    # Companies
    # ---------------------------------
    for company in companies:

        p = company["performance"]
        price = company["price"]

        today_return = p.get("today", 0)

        if best is None or today_return > best["performance"]["today"]:
            best = company

        if worst is None or today_return < worst["performance"]["today"]:
            worst = company

        report += f"""

━━━━━━━━━━━━━━━━━━━━━━

🏢 {company["company"]} ({company["ticker"]})

💲 Close Price   ${price.get("current_price","N/A")}

📈 Today         {today_return:+.2f}%

📅 Month         {p.get("month",0):+.2f}%

🗓️ Year          {p.get("year",0):+.2f}%

📰 Biggest News
"""

        if company["news"]:

            headline = company["news"][0]["title"]

            report += f"{headline}\n"

            headlines.add(headline)

        else:

            report += "No major news.\n"

    # ---------------------------------
    # Winners
    # ---------------------------------
    report += f"""

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🏆 BEST PERFORMER

{best["company"]}

{best["performance"]["today"]:+.2f}%

📉 WORST PERFORMER

{worst["company"]}

{worst["performance"]["today"]:+.2f}%

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📰 TODAY'S BIGGEST STORIES

"""

    for headline in headlines:

        report += f"• {headline}\n"

    report += """

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🤖 ATLAS AI MARKET WRAP

"""

    report += insight

    report += """

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🌙 See you tomorrow!
"""

    return report