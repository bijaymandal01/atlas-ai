from app.services.briefing_ai import is_briefing_request


test_cases = [

    # Should be TRUE
    ("Give me the daily briefing", True),
    ("Show my morning briefing", True),
    ("Give me the morning report", True),
    ("Give me the daily report", True),
    ("Show me the market briefing", True),
    ("Give me today's briefing", True),
    ("Good morning", True),
    ("Brief me", True),
    ("Give me my morning update", True),
    ("Give me the daily update", True),

    # Should be FALSE
    ("Hello", False),
    ("What is Apple?", False),
    ("Compare Apple vs Microsoft", False),
    ("Add Apple to my watchlist", False),
    ("Remove Tesla", False),
    ("Show my watchlist", False),
    ("Show my portfolio", False),
    ("Give me the evening wrap", False),
]


print("=" * 70)
print("DAILY BRIEFING INTENT TEST")
print("=" * 70)

passed = 0
failed = 0

for message, expected in test_cases:

    result = is_briefing_request(message)

    if result == expected:

        print(
            f"PASS | {message} | "
            f"Expected: {expected} | Got: {result}"
        )

        passed += 1

    else:

        print(
            f"FAIL | {message} | "
            f"Expected: {expected} | Got: {result}"
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