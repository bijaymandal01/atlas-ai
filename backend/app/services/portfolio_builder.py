from app.services.finance_service import (
    get_stock_price,
)

from app.services.finance_history import (
    get_stock_performance,
)


def build_portfolio_dashboard(watchlist):

    dashboard = []

    winners = 0
    losers = 0

    for item in watchlist.data:

        company = item["company_name"]
        ticker = item["ticker"]

        price = get_stock_price(ticker)
        performance = get_stock_performance(ticker)

        today = performance.get("today", 0)

        if today >= 0:
            winners += 1
            icon = "🟢"
        else:
            losers += 1
            icon = "🔴"

        dashboard.append({
            "company": company,
            "ticker": ticker,
            "price": price,
            "performance": performance,
            "icon": icon,
        })

    return {
        "companies": dashboard,
        "winners": winners,
        "losers": losers,
    }