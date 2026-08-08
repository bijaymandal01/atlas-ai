def is_briefing_request(message: str) -> bool:

    message = message.lower().strip()

    keywords = [
        "daily briefing",
        "morning briefing",
        "morning report",
        "daily report",
        "market briefing",
        "today's briefing",
        "good morning",
        "brief me",
        "morning update",
        "daily update",
    ]

    return any(keyword in message for keyword in keywords)