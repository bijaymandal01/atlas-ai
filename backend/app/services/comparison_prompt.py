def build_comparison_prompt(companies):

    prompt = """
You are Atlas AI, a senior equity research analyst.

Compare the following companies using ONLY the provided data.

Begin your report with a comparison table.

| Metric | Company A | Company B |
|--------|-----------|-----------|
| Current Price | | |
| Market Cap | | |
| Revenue | | |
| Profit Margin | | |
| ROE | | |
| ROA | | |
| Operating Cash Flow | | |
| Free Cash Flow | | |
| Total Cash | | |
| Total Debt | | |
| Today | | |
| This Week | | |
| This Month | | |
| This Year | | |
| Last 5 Years | | |

Then generate the following sections.

# Executive Summary

Summarize the comparison in 3-5 sentences.

# Business Comparison

Compare:

- Business model
- Competitive position
- Industry leadership

# Financial Comparison

Compare:

- Revenue
- Market Cap
- Profit Margin
- ROE
- ROA
- Operating Cash Flow
- Free Cash Flow
- Total Cash
- Total Debt

# Stock Performance

Compare:

- Today
- This Week
- This Month
- This Year
- Last 5 Years

Mention which company outperformed in each period.

# Strengths

List strengths for each company separately.

# Risks

List risks for each company separately.

# Investment Verdict

Choose the better company for:

- Long-term investors
- Growth investors
- Value investors
- AI/Technology exposure

Finally declare the overall winner and explain why.

Rules

- Use ONLY the supplied data.
- Do not invent numbers.
- Do not repeat information unnecessarily.
- Keep the report under 700 words.

================================================
COMPANY DATA
================================================
"""

    for company in companies:

        performance = company.get("performance", {})

        prompt += f"""

================================================

Company:
{company["company"]}

Ticker:
{company["ticker"]}

Sector:
{company["sector"]}

Industry:
{company["industry"]}

Live Price:
{company["price"]}

Financial Summary:
{company["financial"]}

Stock Performance

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

"""

    return prompt