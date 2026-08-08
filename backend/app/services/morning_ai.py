def detect_morning_intent(message: str):
    """
    Detect whether the user is asking for a Morning Brief.
    """

    message = message.lower().strip()

    keywords = [

        "morning brief",
        "morning briefing",
        "good morning",
        "morning update",
        "daily briefing",
        "today's briefing",
        "today briefing",
        "start my day",
        "morning report",
        "daily report",

    ]

    return any(
        keyword in message
        for keyword in keywords
    )