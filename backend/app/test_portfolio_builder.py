from app.services.portfolio_builder import (
    build_portfolio_dashboard,
)


class MockWatchlist:

    data = [
        {
            "company_name": "Microsoft",
            "ticker": "MSFT",
        },
        {
            "company_name": "Apple",
            "ticker": "AAPL",
        },
        {
            "company_name": "Tesla",
            "ticker": "TSLA",
        },
    ]


print("=" * 70)
print("PORTFOLIO DASHBOARD BUILDER TEST")
print("=" * 70)

watchlist = MockWatchlist()

try:

    portfolio = build_portfolio_dashboard(
        watchlist
    )

    print("\nPORTFOLIO DASHBOARD:")
    print(portfolio)

    print("\n" + "=" * 70)
    print("COMPANIES")
    print("=" * 70)

    for company in portfolio["companies"]:

        print(
            f'{company["icon"]} '
            f'{company["company"]} '
            f'({company["ticker"]})'
        )

        print(
            "Today:",
            company["performance"].get("today")
        )

        print(
            "Week:",
            company["performance"].get("week")
        )

        print(
            "Month:",
            company["performance"].get("month")
        )

        print(
            "Year:",
            company["performance"].get("year")
        )

        print(
            "5 Years:",
            company["performance"].get("five_year")
        )

        print()

    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)

    print(
        "Companies:",
        len(portfolio["companies"])
    )

    print(
        "Winners:",
        portfolio["winners"]
    )

    print(
        "Losers:",
        portfolio["losers"]
    )

    # -----------------------------
    # Validation
    # -----------------------------

    checks = {

        "Portfolio returned":
            bool(portfolio),

        "Companies returned":
            len(portfolio["companies"]) == 3,

        "Winner count valid":
            portfolio["winners"] >= 0,

        "Loser count valid":
            portfolio["losers"] >= 0,

        "Winner + loser count correct":
            (
                portfolio["winners"]
                + portfolio["losers"]
            ) == 3,

        "Company data present":
            all(
                "company" in company
                and "ticker" in company
                and "price" in company
                and "performance" in company
                and "icon" in company
                for company in portfolio["companies"]
            ),

        "Performance data present":
            all(
                "today" in company["performance"]
                for company in portfolio["companies"]
            ),
    }

    print("\n" + "=" * 70)
    print("VALIDATION")
    print("=" * 70)

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