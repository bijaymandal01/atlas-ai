from app.services.comparison_service import compare_companies


print("=" * 70)
print("FULL COMPANY COMPARISON SERVICE TEST")
print("=" * 70)

companies = ["MSFT", "AAPL"]

try:

    result = compare_companies(companies)

    print("\n" + "=" * 70)
    print("ATLAS AI COMPANY COMPARISON")
    print("=" * 70)

    print("\nCOMPANIES:")
    print(result["companies"])

    print("\n" + "=" * 70)
    print("AI COMPARISON REPORT")
    print("=" * 70)

    print(result["report"])

    print("\n" + "=" * 70)
    print("VALIDATION")
    print("=" * 70)

    checks = {

        "Companies data returned":
            bool(result.get("companies")),

        "AI report returned":
            bool(result.get("report", "").strip()),

        "Microsoft present":
            "Microsoft" in result["report"],

        "Apple present":
            "Apple" in result["report"],

        "Executive Summary":
            "Executive Summary" in result["report"],

        "Business Comparison":
            "Business Comparison" in result["report"],

        "Financial Comparison":
            "Financial Comparison" in result["report"],

        "Stock Performance":
            "Stock Performance" in result["report"],

        "Strengths":
            "Strengths" in result["report"],

        "Risks":
            "Risks" in result["report"],

        "Investment Verdict":
            "Investment Verdict" in result["report"],

    }

    passed = 0
    failed = 0

    for name, result_check in checks.items():

        if result_check:
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