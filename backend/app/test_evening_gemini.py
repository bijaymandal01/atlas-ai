from app.services.evening_prompt import build_evening_prompt
from app.services.gemini_service import generate_research


companies = [

    {
        "company": "Microsoft",
        "ticker": "MSFT",
        "performance": {
            "today": 3.46,
            "month": 32.38,
            "year": -1.51,
        },
        "news": [
            {
                "title":
                    "Microsoft Plans Production Boost for AI Chips"
            }
        ],
    },

    {
        "company": "Apple",
        "ticker": "AAPL",
        "performance": {
            "today": -0.92,
            "month": -2.79,
            "year": 35.31,
        },
        "news": [
            {
                "title":
                    "Apple Stock Downgraded to Sell"
            }
        ],
    },

]


print("=" * 70)
print("EVENING GEMINI RESEARCH TEST")
print("=" * 70)


try:

    prompt = build_evening_prompt(companies)

    print("\nPROMPT CREATED: PASS")

    insight = generate_research(prompt)

    print("\nAI INSIGHT:\n")
    print(insight)

    word_count = len(insight.split())

    print("\nWORD COUNT:")
    print(word_count)

    print("\nVALIDATION:")

    checks = {

        "Under 120 words":
            word_count <= 120,

        "Non-empty AI response":
            bool(insight.strip()),

        "Microsoft referenced":
            "Microsoft" in insight,

        "Apple referenced":
            "Apple" in insight,

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