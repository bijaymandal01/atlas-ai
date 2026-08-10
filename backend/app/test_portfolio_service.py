from app.services.portfolio_service import (
    generate_portfolio_report,
)


TEST_TELEGRAM_ID = 9999999997


print("=" * 70)
print("FULL PORTFOLIO SERVICE TEST")
print("=" * 70)

try:

    report = generate_portfolio_report(
        TEST_TELEGRAM_ID
    )

    print("\n" + "=" * 70)
    print("ATLAS AI PORTFOLIO DASHBOARD")
    print("=" * 70)

    print(report)

    print("\n" + "=" * 70)
    print("VALIDATION")
    print("=" * 70)

    checks = {

        "Portfolio Dashboard title":
            "PORTFOLIO DASHBOARD" in report,

        "Companies count":
            "Companies :" in report,

        "Winners section":
            "Winners :" in report,

        "Losers section":
            "Losers :" in report,

        "Microsoft present":
            "Microsoft" in report,

        "Apple present":
            "Apple" in report,

        "Tesla present":
            "Tesla" in report,

        "Best Performer section":
            "BEST PERFORMER TODAY" in report,

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