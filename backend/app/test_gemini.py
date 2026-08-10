from app.services.morning_prompt import build_morning_prompt
from app.services.gemini_service import generate_research


companies = [
    {
        "company": "Microsoft",
        "ticker": "MSFT",
        "performance": {
            "today": 3.26,
            "month": 32.15,
            "year": -1.69,
        },
        "news": [
            {
                "title": "Microsoft plans Maia 300 chip reveal in September",
            },
            {
                "title": "Microsoft Plans Production Boost for AI Chips",
            },
        ],
    },
    {
        "company": "Apple",
        "ticker": "AAPL",
        "performance": {
            "today": -0.92,
            "month": -2.79,
            "year": 35.30,
        },
        "news": [
            {
                "title": "After Earnings, Is Apple Stock a Buy, a Sell, or Fairly Valued?",
            },
            {
                "title": "Future Apple Watches May Include More Screen Sizes",
            },
        ],
    },
]


print("=" * 70)
print("MORNING GEMINI RESEARCH TEST")
print("=" * 70)


try:

    # -----------------------------------------
    # Build prompt
    # -----------------------------------------

    prompt = build_morning_prompt(companies)

    print("\nPROMPT CREATED: PASS")


    # -----------------------------------------
    # Send to Gemini
    # -----------------------------------------

    insight = generate_research(prompt)

    print("\n" + "=" * 70)
    print("ATLAS AI INSIGHT")
    print("=" * 70)

    print(insight)


    # -----------------------------------------
    # Validate response
    # -----------------------------------------

    if not insight or not insight.strip():

        print("\nSTATUS: FAIL")
        print("Gemini returned an empty response.")

    else:

        words = insight.split()

        print("\n" + "=" * 70)
        print("VALIDATION")
        print("=" * 70)

        print(f"WORD COUNT: {len(words)}")

        if len(words) <= 120:
            print("PASS | Under 120 words")
        else:
            print("FAIL | More than 120 words")

        if "Microsoft" in insight or "Apple" in insight:
            print("PASS | Watchlist companies referenced")
        else:
            print("WARNING | No company name referenced")

        if insight.strip():
            print("PASS | Non-empty AI response")

        print("\nSTATUS: PASS")


except Exception as e:

    print("\nSTATUS: FAIL")
    print("ERROR:")
    print(e)