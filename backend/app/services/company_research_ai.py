import re


def detect_company_research_intent(message: str):

    text = message.lower().strip()

    patterns = [
        r"what is (.+)",
        r"tell me about (.+)",
        r"analyze (.+)",
        r"analyse (.+)",
        r"research (.+)",
        r"deep dive (.+)",
        r"deep-dive (.+)",
        r"company analysis (.+)",
        r"analyze company (.+)",
        r"analyse company (.+)",
    ]

    for pattern in patterns:

        match = re.search(pattern, text)

        if match:

            company = match.group(1).strip()

            # Avoid treating questions about financial metrics
            # as company research accidentally.
            if not company:
                return None

            return {
                "intent": "company_research",
                "company": company,
            }

    return None
