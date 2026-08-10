from app.services.comparison_builder import build_company_comparison
from app.services.comparison_prompt import build_comparison_prompt


companies = ["MSFT", "AAPL"]

print("=" * 70)
print("COMPANY COMPARISON PROMPT TEST")
print("=" * 70)

try:

    comparison = build_company_comparison(companies)

    prompt = build_comparison_prompt(comparison)

    print("\nGENERATED PROMPT:\n")
    print(prompt)

    print("\n" + "=" * 70)
    print("VALIDATION")
    print("=" * 70)

    checks = {

        "Atlas AI present":
            "You are Atlas AI" in prompt,

        "Microsoft present":
            "Microsoft Corporation" in prompt,

        "Apple present":
            "Apple Inc." in prompt,

        "MSFT present":
            "MSFT" in prompt,

        "AAPL present":
            "AAPL" in prompt,

        "Comparison table":
            "| Metric | Company A | Company B |" in prompt,

        "Revenue":
            "Revenue" in prompt,

        "Profit Margin":
            "Profit Margin" in prompt,

        "ROE":
            "ROE" in prompt,

        "ROA":
            "ROA" in prompt,

        "Operating Cash Flow":
            "Operating Cash Flow" in prompt,

        "Free Cash Flow":
            "Free Cash Flow" in prompt,

        "Total Debt":
            "Total Debt" in prompt,

        "Stock Performance":
            "Stock Performance" in prompt,

        "Investment Verdict":
            "Investment Verdict" in prompt,

        "Long-term investors":
            "Long-term investors" in prompt,

        "Growth investors":
            "Growth investors" in prompt,

        "Value investors":
            "Value investors" in prompt,

        "AI Technology exposure":
            "AI/Technology exposure" in prompt,

        "No invent numbers instruction":
            "Do not invent numbers" in prompt,

        "700 word limit":
            "under 700 words" in prompt,
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

    print("\nSTATUS: FAIL")
    print("ERROR:")
    print(e)