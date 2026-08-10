from app.services.finance_service import search_company


companies = [
    "Microsoft",
    "Apple",
    "Tesla",
    "Nvidia",
    "Amazon",
    "Meta",
    "Netflix",
]


print("=" * 60)
print("TICKER RESOLUTION TEST")
print("=" * 60)

passed = 0
failed = 0


for company in companies:

    try:

        ticker = search_company(company)

        print(
            f"\n{company}"
            f"\nTicker: {ticker}"
        )

        if ticker:
            print("STATUS: PASS")
            passed += 1
        else:
            print("STATUS: FAIL")
            failed += 1

    except Exception as e:

        print("STATUS: FAIL")
        print("ERROR:", e)

        failed += 1


print("\n" + "=" * 60)
print(f"PASSED: {passed}")
print(f"FAILED: {failed}")
print("=" * 60)