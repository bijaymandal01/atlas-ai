import json

from google import genai

from app.config.settings import (
    GEMINI_API_KEY,
    GEMINI_MODEL
)

client = genai.Client(
    api_key=GEMINI_API_KEY
)

PROMPT = """
You are an AI memory extractor.

Extract ONLY NEW long-term information from the user's latest message.

Return ONLY valid JSON.

Schema:

{
    "role": null,
    "interests_to_add": [],
    "briefing_time": null
}

Rules:

- Only extract long-term information.
- Never extract company names or watchlists.
- Never guess.
- Return valid JSON only.
- If nothing is found, return null or an empty array.

Examples:

User: I am a finance student.
{
    "role": "finance student",
    "interests_to_add": [],
    "briefing_time": null
}

User: Send my briefing every morning.
{
    "role": null,
    "interests_to_add": [],
    "briefing_time": "morning"
}

User: I like AI and investing.
{
    "role": null,
    "interests_to_add": [
        "AI",
        "investing"
    ],
    "briefing_time": null
}

User: Add Apple to my watchlist.
{
    "role": null,
    "interests_to_add": [],
    "briefing_time": null
}
"""


def extract_memory(message: str):

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=f"{PROMPT}\n\nUser:\n{message}"
    )

    try:

        text = response.text.strip()

        if text.startswith("```json"):
            text = (
                text.replace("```json", "")
                .replace("```", "")
                .strip()
            )

        return json.loads(text)

    except Exception:

        return {
            "role": None,
            "interests_to_add": [],
            "briefing_time": None
        }