from app.services.morning_prompt import build_morning_prompt


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
print("MORNING PROMPT BUILDER TEST")
print("=" * 70)

try:

    prompt = build_morning_prompt(companies)

    print("\nGENERATED PROMPT:")
    print("-" * 70)
    print(prompt)
    print("-" * 70)

    # Basic validation
    checks = {
        "Atlas AI present": "You are Atlas AI." in prompt,
        "Microsoft present": "Microsoft" in prompt,
        "Apple present": "Apple" in prompt,
        "Today performance present": "Today:" in prompt,
        "Month performance present": "Month:" in prompt,
        "Year performance present": "Year:" in prompt,
        "News present": "Top Headlines:" in prompt,
        "Instruction present": "Write only the Atlas AI Insight." in prompt,
    }

    print("\nVALIDATION:")

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