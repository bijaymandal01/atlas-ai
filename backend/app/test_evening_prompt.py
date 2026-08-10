from app.services.evening_prompt import build_evening_prompt


mock_companies = [

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
                "title": "Microsoft Plans Production Boost for AI Chips"
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
                "title": "Apple Stock Downgraded to Sell"
            }
        ],
    },
]


print("=" * 70)
print("EVENING PROMPT BUILDER TEST")
print("=" * 70)


prompt = build_evening_prompt(mock_companies)


print("\nGENERATED PROMPT:\n")
print(prompt)


print("\n" + "=" * 70)
print("VALIDATION")
print("=" * 70)


checks = {

    "Atlas AI present":
        "You are Atlas AI." in prompt,

    "Microsoft present":
        "Microsoft" in prompt,

    "Apple present":
        "Apple" in prompt,

    "Today performance present":
        "Today:" in prompt,

    "Month performance present":
        "Month:" in prompt,

    "Year performance present":
        "Year:" in prompt,

    "News present":
        "Microsoft Plans Production Boost for AI Chips" in prompt,

    "Strongest company instruction":
        "strongest company" in prompt,

    "Weakest company instruction":
        "weakest company" in prompt,

    "Opportunity instruction":
        "biggest opportunity" in prompt,

    "Risk instruction":
        "biggest risk" in prompt,

    "No markdown instruction":
        "Do NOT use markdown." in prompt,

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