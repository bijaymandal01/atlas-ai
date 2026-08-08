import feedparser


def get_company_news(company: str, limit: int = 5):
    """
    Fetch latest company news from Google News RSS.
    Removes duplicate headlines.
    """

    url = (
        f"https://news.google.com/rss/search?"
        f"q={company}&hl=en-US&gl=US&ceid=US:en"
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
            "source": getattr(item.source, "title", "Unknown"),
            "published": item.published,
            "link": item.link,
        })

        if len(news) >= limit:
            break

    return news