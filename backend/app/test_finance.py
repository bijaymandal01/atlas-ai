from app.services.finance_service import (
    get_company_info,
    get_stock_price,
    get_financials,
)

print("========== COMPANY ==========")
print(get_company_info("NVDA"))

print("\n========== PRICE ==========")
print(get_stock_price("NVDA"))

print("\n========== FINANCIALS ==========")
financials = get_financials("NVDA")
print(financials.keys())