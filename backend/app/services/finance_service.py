import yfinance as yf


def search_company(company: str):
    """
    Returns the ticker entered by the user.
    For MVP, users can enter tickers directly (AAPL, TSLA, NVDA).
    Later we'll add fuzzy search.
    """
    return company.upper()


def get_company_info(symbol: str):
    """
    Company profile
    """
    ticker = yf.Ticker(symbol)
    info = ticker.info

    return {
        "symbol": symbol,
        "name": info.get("longName"),
        "sector": info.get("sector"),
        "industry": info.get("industry"),
        "country": info.get("country"),
        "website": info.get("website"),
        "employees": info.get("fullTimeEmployees"),
        "market_cap": info.get("marketCap"),
        "currency": info.get("currency"),
        "summary": info.get("longBusinessSummary"),
    }


def get_stock_price(symbol: str):
    """
    Live stock quote
    """
    ticker = yf.Ticker(symbol)
    info = ticker.fast_info

    return {
        "current_price": info.get("lastPrice"),
        "day_high": info.get("dayHigh"),
        "day_low": info.get("dayLow"),
        "previous_close": info.get("previousClose"),
        "market_cap": info.get("marketCap"),
    }


def get_financials(symbol: str):
    """
    Financial statements
    """
    ticker = yf.Ticker(symbol)

    return {
        "income_statement": ticker.financials.to_dict(),
        "balance_sheet": ticker.balance_sheet.to_dict(),
        "cashflow": ticker.cashflow.to_dict(),
    }


def get_history(symbol: str, period="1y"):
    """
    Historical prices
    """
    ticker = yf.Ticker(symbol)

    history = ticker.history(period=period)

    return history.reset_index().to_dict(orient="records")

def get_financial_summary(symbol: str):

    ticker = yf.Ticker(symbol)
    info = ticker.info

    return {
        "market_cap": info.get("marketCap"),
        "trailing_pe": info.get("trailingPE"),
        "forward_pe": info.get("forwardPE"),
        "eps": info.get("trailingEps"),
        "revenue": info.get("totalRevenue"),
        "gross_profit": info.get("grossProfits"),
        "net_income": info.get("netIncomeToCommon"),
        "operating_cashflow": info.get("operatingCashflow"),
        "free_cashflow": info.get("freeCashflow"),
        "total_cash": info.get("totalCash"),
        "total_debt": info.get("totalDebt"),
        "return_on_equity": info.get("returnOnEquity"),
        "return_on_assets": info.get("returnOnAssets"),
        "profit_margin": info.get("profitMargins"),
        "dividend_yield": info.get("dividendYield"),
    }