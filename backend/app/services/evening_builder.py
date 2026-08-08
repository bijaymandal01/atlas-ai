from app.services.finance_service import (
    get_stock_price,
)

from app.services.finance_history import (
    get_stock_performance,
)

from app.services.news_service import (
    get_company_news,
)


def build_evening_data(watchlist):
    """
    Collect data required for the Evening Market Wrap.
    """

    companies = []

    for item in watchlist.data:

        company = item["company_name"]
        ticker = item["ticker"]

        price = get_stock_price(ticker)

        performance = get_stock_performance(ticker)

        news = get_company_news(
            company,
            limit=3
        )

        companies.append({

            "company": company,

            "ticker": ticker,

            "price": price,

            "performance": performance,

            "news": news,

        })

    return companies