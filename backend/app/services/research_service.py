from app.services.finance_service import (
    get_company_info,
    get_stock_price,
    get_financial_summary,
)

from app.services.news_service import get_company_news

from app.services.gemini_service import generate_research


def research_company(company: str):

    symbol = company.upper()

    company_info = get_company_info(symbol)
    stock_price = get_stock_price(symbol)
    financial_summary = get_financial_summary(symbol)
    news = get_company_news(symbol)

    prompt = f"""
You are Atlas AI, a professional equity research analyst.

Generate a concise but professional equity research report.

=========================
COMPANY PROFILE
=========================

Name: {company_info.get("name")}
Sector: {company_info.get("sector")}
Industry: {company_info.get("industry")}
Country: {company_info.get("country")}
Market Cap: {company_info.get("market_cap")}
Employees: {company_info.get("employees")}

Business Summary:

{company_info.get("summary")}

=========================
LIVE STOCK DATA
=========================

Current Price: {stock_price.get("current_price")}
Previous Close: {stock_price.get("previous_close")}
Day High: {stock_price.get("day_high")}
Day Low: {stock_price.get("day_low")}

=========================
KEY FINANCIAL METRICS
=========================

{financial_summary}

=========================
LATEST NEWS
=========================

{news}

=========================
Generate the report in this format:

1. Executive Summary

2. Company Overview

3. Financial Highlights

4. Latest News Summary

5. Strengths

6. Risks

7. Investment Outlook

Keep the report professional, concise, and easy to read.
"""

    report = generate_research(prompt)

    return {
        "symbol": symbol,
        "company": company_info,
        "price": stock_price,
        "financials": financial_summary,
        "news": news,
        "report": report,
    }