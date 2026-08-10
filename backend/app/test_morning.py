from app.services.morning_ai import detect_morning_intent


tests = {
    "Good morning": True,
    "Give me my morning brief": True,
    "Show my morning briefing": True,
    "I want my morning update": True,
    "Give me today's briefing": True,
    "Start my day": True,
    "Show my morning report": True,
    "Give me the daily report": True,

    "Hello": False,
    "What is Apple?": False,
    "Compare Apple vs Microsoft": False,
    "Add Apple to my watchlist": False,
    "Remove Tesla": False,
    "Show my portfolio": False,
}


passed = 0
failed = 0


for message, expected in tests.items():

    result = detect_morning_intent(message)

    status = "PASS" if result == expected else "FAIL"

    print(
        f"{status} | "
        f"{message} | "
        f"Expected: {expected} | "
        f"Got: {result}"
    )

    if result == expected:
        passed += 1
    else:
        failed += 1


print("\n" + "=" * 60)
print(f"PASSED: {passed}")
print(f"FAILED: {failed}")
print("=" * 60)