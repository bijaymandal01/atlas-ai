from app.services.comparison_builder import build_company_comparison


companies = ["MSFT", "AAPL"]

print("=" * 60)
print("COMPANY COMPARISON BUILDER TEST")
print("=" * 60)

try:

    result = build_company_comparison(companies)

    print("\nCOMPARISON DATA:")
    print(result)

    if len(result) != 2:
        print("\nSTATUS: FAIL")
        print("Expected 2 companies.")

    else:

        for company in result:

            print("\n" + "=" * 40)

            print("COMPANY:")
            print(company["company"])

            print("TICKER:")
            print(company["ticker"])

            print("SECTOR:")
            print(company["sector"])

            print("INDUSTRY:")
            print(company["industry"])

            print("PRICE:")
            print(company["price"])

            print("FINANCIAL:")
            print(company["financial"])

            print("PERFORMANCE:")
            print(company["performance"])

        print("\nSTATUS: PASS")

except Exception as e:

    print("\nSTATUS: FAIL")
    print("ERROR:")
    print(e)
    