from app.services.memory_extractor import extract_memory


TEST_MESSAGES = [
    "I am a finance student.",
    "I prefer US stocks.",
    "Send my briefing every morning.",
    "I like AI and investing.",
    "Add Apple to my watchlist.",
    "Compare Apple vs Meta.",
    "Hello, how are you?",
]


for message in TEST_MESSAGES:

    print("=" * 70)
    print("USER:")
    print(message)

    result = extract_memory(message)

    print("\nEXTRACTED MEMORY:")
    print(result)