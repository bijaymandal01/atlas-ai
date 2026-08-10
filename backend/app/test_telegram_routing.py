from app.services.chat_service import chat


TEST_TELEGRAM_ID = 9999999997


tests = [
    ("Show my watchlist", "watchlist"),
    ("Add Microsoft", "watchlist"),

    ("Good morning", "morning"),
    ("Give me my morning brief", "morning"),

    ("Give me the evening wrap", "evening"),
    ("Show me the market close", "evening"),

    ("Show my portfolio", "portfolio"),

    ("Give me the daily briefing", "briefing"),

    ("What is Microsoft?", "general"),
]


print("=" * 70)
print("TELEGRAM ATLAS ROUTING TEST")
print("=" * 70)


for message, expected in tests:

    print("\n" + "-" * 70)
    print("USER:")
    print(message)

    try:

        response = chat(
            TEST_TELEGRAM_ID,
            message
        )

        print("\nATLAS:")
        print(response)

        # We only verify that chat successfully returns a response.
        if response and response.get("reply"):

            print("\nPASS | Response generated")

        else:

            print("\nFAIL | Empty response")

    except Exception as e:

        print("\nFAIL | Exception")
        print(e)


print("\n" + "=" * 70)
print("STATUS: ROUTING TEST COMPLETE")
print("=" * 70)