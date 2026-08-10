from app.services.comparison_builder import build_company_comparison
from app.services.comparison_prompt import build_comparison_prompt
from app.services.gemini_service import generate_research


companies = ["MSFT", "AAPL"]

print("=" * 70)
print("COMPANY COMPARISON GEMINI RESEARCH TEST")
print("=" * 70)

try:

    comparison = build_company_comparison(companies)

    prompt = build_comparison_prompt(comparison)

    print("\nPROMPT CREATED: PASS")

    report = generate_research(prompt)

    print("\nAI COMPARISON REPORT:\n")
    print(report)

    print("\n" + "=" * 70)
    print("VALIDATION")
    print("=" * 70)

    checks = {

        "Non-empty AI response":
            bool(report.strip()),

        "Microsoft referenced":
            "Microsoft" in report,

        "Apple referenced":
            "Apple" in report,

        "Executive Summary":
            "Executive Summary" in report,

        "Business Comparison":
            "Business Comparison" in report,

        "Financial Comparison":
            "Financial Comparison" in report,

        "Stock Performance":
            "Stock Performance" in report,

        "Strengths":
            "Strengths" in report,

        "Risks":
            "Risks" in report,

        "Investment Verdict":
            "Investment Verdict" in report,

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