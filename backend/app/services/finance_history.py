import yfinance as yf


def get_stock_performance(symbol: str):

    stock = yf.Ticker(symbol)

    periods = {
        "today": "5d",
        "week": "5d",
        "month": "1mo",
        "year": "1y",
        "five_year": "5y",
    }

    performance = {}

    for key, period in periods.items():

        history = stock.history(period=period)

        if history.empty:
            performance[key] = None
            continue

        first = history["Close"].iloc[0]
        last = history["Close"].iloc[-1]

        change = ((last - first) / first) * 100

        performance[key] = round(change, 2)

    return performance