from app.services.briefing_builder import (
    build_briefing_dashboard,
)

from app.services.briefing_prompt import (
    build_briefing_prompt,
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
print("DAILY BRIEFING PROMPT TEST")
print("=" * 70)

try:

    dashboard = build_briefing_dashboard(
        MockWatchlist()
    )

    prompt = build_briefing_prompt(
        dashboard
    )

    print("\n" + "=" * 70)
    print("GENERATED PROMPT")
    print("=" * 70)

    print(prompt)

    print("\n" + "=" * 70)
    print("VALIDATION")
    print("=" * 70)

    checks = {

        "Atlas AI present":
            "Atlas AI" in prompt,

        "Dashboard present":
            dashboard in prompt,

        "Executive Summary":
            "Executive Summary" in prompt,

        "Market Themes":
            "Market Themes" in prompt,

        "Risks":
            "Risks" in prompt,

        "Atlas Insight":
            "Atlas Insight" in prompt,

        "Watch Today":
            "Watch Today" in prompt,

        "No price repetition instruction":
            "Do not repeat stock prices" in prompt,

        "No headline repetition instruction":
            "Do not repeat news headlines" in prompt,

        "400 word limit":
            "400 words" in prompt,

        "Bloomberg style":
            "Bloomberg-style" in prompt,

        "Markdown instruction":
            "markdown headings and bullet points" in prompt,
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