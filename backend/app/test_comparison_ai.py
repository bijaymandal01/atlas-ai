from app.services.comparison_ai import detect_comparison_intent


tests = [

    ("Compare Apple vs Microsoft", True),
    ("Compare Apple with Microsoft", True),
    ("Apple vs Microsoft", True),
    ("Microsoft versus Apple", True),
    ("Compare Nvidia and AMD", True),
    ("Which is better Apple or Microsoft?", True),
    ("What is the difference between Tesla and Nvidia?", True),

    ("Hello", False),
    ("Good morning", False),
    ("Tell me about Apple", False),
    ("Analyze Microsoft", False),
    ("Show my portfolio", False),
    ("Show my watchlist", False),
    ("Give me my morning brief", False),
    ("Give me the evening wrap", False),
    ("Add Apple to my watchlist", False),
    ("Remove Tesla", False),
]

print("=" * 70)
print("COMPANY COMPARISON INTENT TEST")
print("=" * 70)

passed = 0
failed = 0

for message, expected in tests:

    result = detect_comparison_intent(message)

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