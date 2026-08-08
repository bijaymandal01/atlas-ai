def build_evening_prompt(companies):

    prompt = """
You are Atlas AI.

Write ONLY the "Atlas AI Market Wrap" section.

Requirements:

- Maximum 120 words.
- Summarize today's trading session.
- Mention today's strongest company.
- Mention today's weakest company.
- Mention today's biggest opportunity.
- Mention today's biggest risk.
- Do NOT repeat prices.
- Do NOT repeat headlines.
- Do NOT use markdown.
- Return only the insight.

================================================
"""

    for company in companies:

        p = company["performance"]

        prompt += f"""

Company: {company["company"]}

Today:
{p.get("today","N/A")}%

Month:
{p.get("month","N/A")}%

Year:
{p.get("year","N/A")}%

"""

        if company["news"]:

            prompt += "Headline:\n"

            prompt += company["news"][0]["title"]

            prompt += "\n"

    return prompt