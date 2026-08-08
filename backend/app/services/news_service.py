import feedparser
from urllib.parse import quote


def get_company_news(company: str, limit: int = 5):
    """
    Fetch latest company news from Google News RSS.
    Removes duplicate headlines.
    """

    query = quote(company)

    url = (
        f"https://news.google.com/rss/search?"
        f"q={query}&hl=en-US&gl=US&ceid=US:en"
    )

    feed = feedparser.parse(url)

    news = []
    seen_titles = set()

    for item in feed.entries:

        title = item.title.strip()

        if title in seen_titles:
            continue

        seen_titles.add(title)

        news.append({
            "title": title,
            "source": getattr(getattr(item, "source", None), "title", "Unknown"),
            "published": getattr(item, "published", "Unknown"),
            "link": item.link,
        })

        if len(news) >= limit:
            break

    return news