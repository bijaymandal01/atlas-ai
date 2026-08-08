from app.services.news_service import get_company_news

news = get_company_news("NVDA")

print(news)