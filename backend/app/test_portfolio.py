from app.services.portfolio_service import (
    generate_portfolio_report,
)

TELEGRAM_USER_ID = 123456789

print("=" * 80)
print("PORTFOLIO REPORT")
print("=" * 80)

print(generate_portfolio_report(TELEGRAM_USER_ID))