def detect_evening_intent(message: str):
    """
    Detect whether the user is asking for the Evening Market Wrap.
    """

    message = message.lower().strip()

    keywords = [

        "evening wrap",
        "market wrap",
        "market close",
        "after market",
        "after market close",
        "evening briefing",
        "evening brief",
        "end of day",
        "end of day report",
        "market summary",
        "today's market wrap",
        "today market wrap",
        "wrap today's market",
        "wrap up today's market",

    ]

    return any(
        keyword in message
        for keyword in keywords
    )