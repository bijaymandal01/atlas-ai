from app.services.chat_service import chat


TEST_USER_ID = 9999999997

tests = [
    "Compare Apple vs Microsoft",
    "Compare Tesla vs Nvidia",
    "Tell me about Apple",
    "Analyze Microsoft",
    "Show my portfolio",
    "Show my watchlist",
]

print("=" * 70)
print("CHAT SERVICE — COMPARISON INTEGRATION TEST")
print("=" * 70)

for message in tests:

    print("\n" + "-" * 70)
    print("USER:")
    print(message)

    try:

        response = chat(
            TEST_USER_ID,
            message
        )

        print("\nATLAS:")
        print(response["reply"])

        print("\nSTATUS: PASS")

    except Exception as e:

        print("\nSTATUS: FAIL")
        print("ERROR:")
        print(e)