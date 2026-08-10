from app.services.portfolio_ai import detect_portfolio_intent


test_cases = [

    # Should be TRUE
    ("Show my portfolio", True),
    ("Open my portfolio", True),
    ("Show portfolio dashboard", True),
    ("Give me my portfolio report", True),
    ("Give me a portfolio summary", True),
    ("Show my investments", True),
    ("Show my holdings", True),
    ("What's in my portfolio?", True),

    # Should be FALSE
    ("Hello", False),
    ("Good morning", False),
    ("Give me my morning brief", False),
    ("Give me the evening wrap", False),
    ("Show my watchlist", False),
    ("Add Apple to my watchlist", False),
    ("Remove Tesla", False),
    ("Compare Apple vs Microsoft", False),
    ("What is Apple's revenue?", False),
]


print("=" * 70)
print("PORTFOLIO INTENT TEST")
print("=" * 70)

passed = 0
failed = 0

for message, expected in test_cases:

    result = detect_portfolio_intent(message)

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