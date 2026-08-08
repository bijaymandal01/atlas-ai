from app.services.comparison_service import compare_companies

companies = [
    "NVDA",
    "AMD",
]

result = compare_companies(companies)

print("=" * 80)
print("COMPANY COMPARISON")
print("=" * 80)

print(result["report"])