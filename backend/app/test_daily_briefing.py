from app.services.briefing_service import (
    generate_daily_briefing,
)


TEST_TELEGRAM_ID = 9999999997


print("=" * 70)
print("FULL DAILY BRIEFING SERVICE TEST")
print("=" * 70)


try:

    # ---------------------------------
    # Generate Daily Briefing
    # ---------------------------------

    report = generate_daily_briefing(
        TEST_TELEGRAM_ID
    )

    print("\n" + "=" * 70)
    print("ATLAS AI DAILY BRIEFING")
    print("=" * 70)

    print(report)

    # ---------------------------------
    # Validation
    # ---------------------------------

    print("\n" + "=" * 70)
    print("VALIDATION")
    print("=" * 70)

    checks = {

        "Daily Brief title":
            "ATLAS AI DAILY BRIEF" in report,

        "Market Snapshot":
            "MARKET SNAPSHOT" in report,

        "Watchlist section":
            "WATCHLIST" in report,

        "Microsoft present":
            "MICROSOFT" in report,

        "Apple present":
            "APPLE" in report,

        "Tesla present":
            "TESLA" in report,

        "Executive Summary":
            "Executive Summary" in report,

        "Market Themes":
            "Market Themes" in report,

        "Risks":
            "Risks" in report,

        "Atlas Insight":
            "Atlas Insight" in report,

        "Watch Today":
            "Watch Today" in report,

        "AI analysis present":
            "🤖 ATLAS AI INSIGHT" in report,

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