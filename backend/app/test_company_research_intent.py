from app.services.company_research_ai import (
    detect_company_research_intent,
)


tests = [

    ("What is Microsoft?", True),
    ("Tell me about Apple", True),
    ("Analyze Nvidia", True),
    ("Analyse Tesla", True),
    ("Research Amazon", True),
    ("Deep dive into Microsoft", True),
    ("Give me a deep-dive on Apple", True),

    ("Hello", False),
    ("Good morning", False),
    ("Show my watchlist", False),
    ("Show my portfolio", False),
    ("Give me my morning brief", False),
    ("Give me the evening wrap", False),
    ("Compare Apple vs Microsoft", False),
    ("Add Apple to my watchlist", False),
    ("Remove Tesla", False),
]


print("=" * 70)
print("COMPANY RESEARCH INTENT TEST")
print("=" * 70)


passed = 0
failed = 0


for message, expected in tests:

    result = detect_company_research_intent(message)

    actual = result is not None

    if actual == expected:

        print(
            f"PASS | {message} | "
            f"Expected: {expected} | Got: {actual}"
        )

        passed += 1

    else:

        print(
            f"FAIL | {message} | "
            f"Expected: {expected} | Got: {actual}"
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