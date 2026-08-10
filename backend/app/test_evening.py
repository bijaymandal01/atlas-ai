from app.services.evening_ai import detect_evening_intent


tests = [

    # -----------------------------
    # SHOULD PASS
    # -----------------------------

    ("Good evening, give me my evening wrap", True),

    ("Give me the market wrap", True),

    ("Show me the market close", True),

    ("What happened after market close?", True),

    ("Give me my evening briefing", True),

    ("Give me my evening brief", True),

    ("Show me the end of day report", True),

    ("Give me today's market summary", True),

    ("Show today's market wrap", True),

    ("Wrap today's market", True),

    ("Wrap up today's market", True),


    # -----------------------------
    # SHOULD NOT TRIGGER
    # -----------------------------

    ("Hello", False),

    ("Good morning", False),

    ("Show my portfolio", False),

    ("Show my watchlist", False),

    ("Add Apple to my watchlist", False),

    ("Remove Tesla", False),

    ("Compare Apple vs Microsoft", False),

    ("What is Apple's revenue?", False),

    ("Tell me about Nvidia", False),

]


passed = 0
failed = 0


print("=" * 70)
print("EVENING INTENT TEST")
print("=" * 70)


for message, expected in tests:

    result = detect_evening_intent(message)

    if result == expected:

        print(
            f"PASS | {message} "
            f"| Expected: {expected} "
            f"| Got: {result}"
        )

        passed += 1

    else:

        print(
            f"FAIL | {message} "
            f"| Expected: {expected} "
            f"| Got: {result}"
        )

        failed += 1


print("\n" + "=" * 70)
print(f"PASSED: {passed}")
print(f"FAILED: {failed}")
print("=" * 70)


if failed == 0:
    print("STATUS: PASS")
else:
    print("STATUS: FAIL")