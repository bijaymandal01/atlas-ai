from app.services.finance_service import get_financial_summary

summary = get_financial_summary("NVDA")

print(summary)