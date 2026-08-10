def detect_comparison_intent(message: str):
    """
    Detect whether the user is asking to compare companies.
    """

    message = message.lower().strip()

    keywords = [
        "compare",
        "comparison",
        "compare vs",
        "compare with",
        "compare between",
        "versus",
        "vs",
        "difference between",
        "which is better",
        "better than",
    ]

    return any(
        keyword in message
        for keyword in keywords
    )
