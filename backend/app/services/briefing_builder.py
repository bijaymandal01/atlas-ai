from datetime import datetime

from app.services.finance_service import get_stock_price
from app.services.news_service import get_company_news


def build_briefing_dashboard(watchlist):

    today = datetime.now().strftime("%d %b %Y")

    total_companies = len(watchlist.data)
    positive = 0
    negative = 0
    neutral = 0

    company_sections = ""

    for item in watchlist.data:

        company = item["company_name"]
        ticker = item["ticker"]

        price = get_stock_price(ticker)
        news = get_company_news(company)

        current = price.get("current_price") or 0
        previous = price.get("previous_close") or current
        high = price.get("day_high") or current
        low = price.get("day_low") or current

        change = current - previous

        if previous:
            change_percent = (change / previous) * 100
        else:
            change_percent = 0

        if change > 0:
            arrow = "🟢"
            sign = "+"
            positive += 1

        elif change < 0:
            arrow = "🔴"
            sign = ""
            negative += 1

        else:
            arrow = "🟡"
            sign = ""
            neutral += 1

        company_sections += f"""

────────────────────────────────────

🏢 {company.upper()}
📈 Ticker : {ticker}

💲 Current : ${current:.2f}
{arrow} Change  : {sign}{change:.2f} ({sign}{change_percent:.2f}%)

📈 High    : ${high:.2f}
📉 Low     : ${low:.2f}

📰 Headlines
"""

        if news:

            for index, article in enumerate(news[:2], start=1):

                company_sections += f"""

{index}. {article["source"]}

   {article["title"]}

"""

        else:

            company_sections += """

• No major news today.

"""

    dashboard = f"""
🌅 ATLAS AI DAILY BRIEF

📅 {today}

════════════════════════════════════

📊 MARKET SNAPSHOT

🏢 Companies : {total_companies}
🟢 Positive : {positive}
🔴 Negative : {negative}
🟡 Unchanged : {neutral}

════════════════════════════════════

📊 WATCHLIST
"""

    dashboard += company_sections

    dashboard += """

════════════════════════════════════
"""

    return dashboard