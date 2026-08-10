from app.services.evening_builder import build_evening_data


class MockWatchlist:

    data = [
        {
            "company_name": "Microsoft",
            "ticker": "MSFT",
        }
    ]


print("=" * 60)
print("EVENING DATA BUILDER — VALID TICKER TEST")
print("=" * 60)

watchlist = MockWatchlist()

try:

    companies = build_evening_data(watchlist)

    print("\nEVENING DATA:")
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
            and performance.get("today") is not None
            and performance.get("year") is not None
            and len(company["news"]) > 0
        ):

            print("\nSTATUS: PASS")

        else:

            print("\nSTATUS: FAIL")
            print("Evening market data is missing.")


except Exception as e:

    print("\nSTATUS: FAIL")
    print("ERROR:")
    print(e)