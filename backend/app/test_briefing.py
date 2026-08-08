from app.services.briefing_service import generate_daily_briefing

# Replace with your Telegram User ID
TELEGRAM_USER_ID = 123456789

print("=" * 80)
print("ATLAS AI - DAILY BRIEFING TEST")
print("=" * 80)

report = generate_daily_briefing(TELEGRAM_USER_ID)

print(report)

print("=" * 80)
print("TEST COMPLETED")
print("=" * 80)