from app.services.morning_builder import build_morning_data


class MockWatchlist:
    data = [
        {
            "company_name": "Microsoft",
            "ticker": "MSFT",
        }
    ]


print("=" * 60)
print("MORNING DATA BUILDER — VALID TICKER TEST")
print("=" * 60)

watchlist = MockWatchlist()

try:

    companies = build_morning_data(watchlist)

    print("\nMORNING DATA:")
    print(companies)

    if not companies:
        print("\nSTATUS: FAIL")
        print("No data returned.")

    else:

        company = companies[0]

        print("\nCOMPANY:")
        print(company["company"])

        print("\nTICKER:")
        print(company["ticker"])

        print("\nPRICE:")
        print(company["price"])

        print("\nPERFORMANCE:")
        print(company["performance"])

        print("\nNEWS COUNT:")
        print(len(company["news"]))

        price = company["price"]

        performance = company["performance"]

        if (
            price.get("current_price") is not None
            and performance.get("year") is not None
        ):
            print("\nSTATUS: PASS")

        else:
            print("\nSTATUS: FAIL")
            print("Market data is missing.")

except Exception as e:

    print("\nSTATUS: FAIL")
    print("ERROR:")
    print(e)