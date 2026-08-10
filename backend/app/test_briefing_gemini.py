from app.services.briefing_builder import (
    build_briefing_dashboard,
)

from app.services.briefing_prompt import (
    build_briefing_prompt,
)

from app.services.gemini_service import (
    generate_research,
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
print("DAILY BRIEFING GEMINI RESEARCH TEST")
print("=" * 70)

try:

    # -----------------------------
    # Build Dashboard
    # -----------------------------

    dashboard = build_briefing_dashboard(
        MockWatchlist()
    )

    # -----------------------------
    # Build Prompt
    # -----------------------------

    prompt = build_briefing_prompt(
        dashboard
    )

    print("\nPROMPT CREATED: PASS")

    # -----------------------------
    # Gemini
    # -----------------------------

    analysis = generate_research(
        prompt
    )

    print("\n" + "=" * 70)
    print("AI ANALYSIS")
    print("=" * 70)

    print(analysis)

    # -----------------------------
    # Validation
    # -----------------------------

    print("\n" + "=" * 70)
    print("VALIDATION")
    print("=" * 70)

    word_count = len(
        analysis.split()
    )

    checks = {

        "Non-empty AI response":
            bool(analysis.strip()),

        "Under 400 words":
            word_count <= 400,

        "Microsoft referenced":
            "Microsoft" in analysis,

        "Apple referenced":
            "Apple" in analysis,

        "Tesla referenced":
            "Tesla" in analysis,

        "Executive Summary":
            "Executive Summary" in analysis,

        "Market Themes":
            "Market Themes" in analysis,

        "Risks":
            "Risks" in analysis,

        "Atlas Insight":
            "Atlas Insight" in analysis,

        "Watch Today":
            "Watch Today" in analysis,

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

    print("\nWORD COUNT:")
    print(word_count)

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