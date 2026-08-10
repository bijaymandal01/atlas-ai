from app.services.morning_service import generate_morning_brief


TEST_TELEGRAM_ID = 9999999997


print("=" * 70)
print("FULL MORNING BRIEF SERVICE TEST")
print("=" * 70)

try:

    report = generate_morning_brief(
        TEST_TELEGRAM_ID
    )

    print("\n" + "=" * 70)
    print("ATLAS AI MORNING BRIEF")
    print("=" * 70)

    print(report)

    print("\n" + "=" * 70)
    print("VALIDATION")
    print("=" * 70)

    checks = {
        "Morning Brief title":
            "ATLAS AI MORNING BRIEF" in report,

        "Watchlist section":
            "YOUR WATCHLIST" in report,

        "Market Headlines section":
            "MARKET HEADLINES" in report,

        "Today's Focus section":
            "TODAY'S FOCUS" in report,

        "AI Insight section":
            "ATLAS AI INSIGHT" in report,

        "Productive trading message":
            "Have a productive trading day!" in report,

        "Report is not empty":
            bool(report.strip()),
    }

    passed = 0
    failed = 0

    for name, result in checks.items():

        if result:
            print(f"PASS | {name}")
            passed += 1

        else:
            print(f"FAIL | {name}")
            failed += 1

    print("\n" + "=" * 70)
    print(f"PASSED: {passed}")
    print(f"FAILED: {failed}")
    print("=" * 70)

    if failed == 0:
        print("STATUS: PASS")
    else:
        print("STATUS: FAIL")


except Exception as e:

    print("\n" + "=" * 70)
    print("STATUS: FAIL")
    print("=" * 70)

    print("ERROR:")
    print(e)