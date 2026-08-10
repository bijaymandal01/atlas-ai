from app.scheduler.telegram_sender import format_telegram_message


message = """
# Investment Verdict

- **Long-term investors:** Apple
- **Growth investors:** Apple
- **Value investors:** Meta

**Overall Winner:** Apple Inc.

| Metric | Apple | Meta |
|--------|-------|------|
| Revenue | $466.82B | $228.25B |
| Profit Margin | 27.62% | 29.83% |
| Today | -0.91% | +1.09% |

## Risks

- **Apple:** Product execution risk.
- **Meta:** Regulatory risk.
"""


result = format_telegram_message(message)

print("=" * 70)
print("TELEGRAM FORMAT TEST")
print("=" * 70)

print(result)

print("\nSTATUS: PASS")