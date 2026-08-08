def detect_portfolio_intent(message: str):

    message = message.lower()

    keywords = [
        "portfolio",
        "my portfolio",
        "portfolio dashboard",
        "portfolio report",
        "portfolio summary",
        "investments",
        "holdings",
    ]

    return any(keyword in message for keyword in keywords)