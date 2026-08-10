from app.services.evening_service import generate_evening_wrap


TEST_TELEGRAM_ID = 9999999997


print("=" * 70)
print("FULL EVENING MARKET WRAP SERVICE TEST")
print("=" * 70)

try:

    report = generate_evening_wrap(
        TEST_TELEGRAM_ID
    )

    print("\n" + "=" * 70)
    print("ATLAS AI EVENING MARKET WRAP")
    print("=" * 70)

    print(report)

    print("\n" + "=" * 70)
    print("VALIDATION")
    print("=" * 70)

    checks = {

        "Evening Wrap title":
            "ATLAS AI MARKET WRAP" in report,

        "Watchlist section":
            "TODAY'S WATCHLIST" in report,

        "Best Performer section":
            "BEST PERFORMER" in report,

        "Worst Performer section":
            "WORST PERFORMER" in report,

        "Biggest Stories section":
            "TODAY'S BIGGEST STORIES" in report,

        "AI Market Wrap section":
            "ATLAS AI MARKET WRAP" in report,

        "Tomorrow message":
            "See you tomorrow!" in report,

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