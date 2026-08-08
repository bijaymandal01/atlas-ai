from app.services.evening_service import (
    generate_evening_wrap,
)

# Your Telegram User ID
TELEGRAM_USER_ID = 123456789

print("=" * 80)
print("🌆 ATLAS AI EVENING WRAP TEST")
print("=" * 80)

report = generate_evening_wrap(
    TELEGRAM_USER_ID
)

print(report)