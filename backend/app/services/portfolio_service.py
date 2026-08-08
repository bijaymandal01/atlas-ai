from app.database.user_service import get_user
from app.database.watchlist_service import get_watchlist

from app.services.portfolio_builder import (
    build_portfolio_dashboard,
)


def generate_portfolio_report(telegram_user_id: int):

    user = get_user(telegram_user_id)

    if not user.data:
        return "❌ User not found."

    user_id = user.data[0]["id"]

    watchlist = get_watchlist(user_id)

    if not watchlist.data:
        return "📊 Your watchlist is empty."

    portfolio = build_portfolio_dashboard(watchlist)

    report = f"""
📊 PORTFOLIO DASHBOARD

🏢 Companies : {len(portfolio["companies"])}

🟢 Winners : {portfolio["winners"]}

🔴 Losers : {portfolio["losers"]}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

    best_today = None

    for stock in portfolio["companies"]:

        p = stock["performance"]

        report += f"""
{stock["icon"]} {stock["company"]} ({stock["ticker"]})

Today       {p["today"]:+.2f}%
Week        {p["week"]:+.2f}%
Month       {p["month"]:+.2f}%
Year        {p["year"]:+.2f}%
5 Years     {p["five_year"]:+.2f}%

━━━━━━━━━━━━━━━━━━━━━━
"""

        if best_today is None or p["today"] > best_today["performance"]["today"]:
            best_today = stock

    report += f"""

🏆 BEST PERFORMER TODAY

{best_today["company"]}

{best_today["performance"]["today"]:+.2f}%
"""

    return report