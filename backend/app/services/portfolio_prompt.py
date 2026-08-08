def build_portfolio_prompt(portfolio):

    prompt = """
You are Atlas AI, a senior portfolio analyst.

Analyze the user's investment portfolio.

Use ONLY the provided data.

Generate a professional report using the following structure.

# Portfolio Overview

Summarize the portfolio in 3-5 sentences.

# Top Performers

Identify:

- Best performer today
- Best performer this week
- Best performer this month
- Best performer this year
- Best performer over the last 5 years

Explain why.

# Portfolio Financial Health

Compare companies using:

- Market Cap
- Revenue
- Profit Margin
- ROE
- ROA
- Operating Cash Flow
- Free Cash Flow
- Total Cash
- Total Debt

Highlight which companies are financially strongest.

# Sector Allocation

List all sectors represented in the portfolio.

Comment on diversification.

# Portfolio Risks

Identify:

- Concentration risk
- Sector risk
- Financial risk
- Valuation risk

# Atlas AI Recommendation

Provide practical suggestions for improving the portfolio.

Rules

- Use ONLY supplied data.
- Never invent numbers.
- Keep the report under 700 words.

====================================================
PORTFOLIO DATA
====================================================
"""

    for company in portfolio:

        performance = company.get("performance", {})

        prompt += f"""

====================================================

Company:
{company["company"]}

Ticker:
{company["ticker"]}

Company Information:
{company["info"]}

Live Price:
{company["price"]}

Financial Summary:
{company["financial"]}

Performance

Today:
{performance.get("today", "N/A")}%

This Week:
{performance.get("week", "N/A")}%

This Month:
{performance.get("month", "N/A")}%

This Year:
{performance.get("year", "N/A")}%

Last 5 Years:
{performance.get("five_year", "N/A")}%

Latest News:
"""

        news = company.get("news", [])

        if news:

            for article in news:

                prompt += f"""

Title:
{article["title"]}

Source:
{article["source"]}

"""

        else:

            prompt += """

No major news available.

"""

    return prompt