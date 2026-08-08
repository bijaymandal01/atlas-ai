from app.services.morning_service import (
    generate_morning_brief,
)

# Your Telegram User ID
TELEGRAM_USER_ID = 123456789

print("=" * 80)
print("🌅 ATLAS AI MORNING BRIEF TEST")
print("=" * 80)

report = generate_morning_brief(
    TELEGRAM_USER_ID
)

print(report)