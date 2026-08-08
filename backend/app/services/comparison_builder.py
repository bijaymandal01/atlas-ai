from app.services.finance_history import get_stock_performance
from app.services.finance_service import (
    get_company_info,
    get_stock_price,
    get_financial_summary,
)


def build_company_comparison(companies):

    comparison = []

    for ticker in companies:

        info = get_company_info(ticker)
        price = get_stock_price(ticker)
        financial = get_financial_summary(ticker)

        performance = get_stock_performance(ticker)

        comparison.append({

            "ticker": ticker,

            "company": info.get("name"),

            "sector": info.get("sector"),

            "industry": info.get("industry"),

            "price": price,

            "financial": financial,

            "performance": performance,

        })

    return comparison