def build_morning_prompt(companies):

    prompt = """
You are Atlas AI.

Write ONLY the "Atlas AI Insight" section for today's Morning Brief.

Requirements:

- Maximum 120 words.
- 3 to 5 concise sentences.
- Analyze only the supplied watchlist.
- Summarize the overall outlook.
- Mention the most important company if necessary.
- Mention the biggest opportunity.
- Mention the biggest risk.
- Do NOT repeat stock prices.
- Do NOT repeat performance numbers.
- Do NOT repeat news headlines.
- Do NOT use markdown.
- Do NOT use headings.
- Return only the insight text.

====================================================
WATCHLIST SUMMARY
====================================================
"""

    for company in companies:

        performance = company.get("performance", {})
        news = company.get("news", [])

        prompt += f"""

Company:
{company["company"]}

Today:
{performance.get("today", "N/A")}%

Month:
{performance.get("month", "N/A")}%

Year:
{performance.get("year", "N/A")}%

"""

        if news:

            prompt += "Top Headlines:\n"

            for article in news[:2]:
                prompt += f"- {article['title']}\n"

        else:

            prompt += "No major news.\n"

    prompt += """

Write only the Atlas AI Insight.
"""

    return prompt