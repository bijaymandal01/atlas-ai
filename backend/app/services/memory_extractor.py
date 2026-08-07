import json

from google import genai

from app.config.settings import (
    GEMINI_API_KEY,
    GEMINI_MODEL
)

client = genai.Client(api_key=GEMINI_API_KEY)

PROMPT = """
You are an AI memory extractor.

Extract ONLY NEW long-term information from the user's latest message.

Return ONLY valid JSON.

Schema:

{
    "role": null,
    "companies_to_add": [],
    "interests_to_add": [],
    "briefing_time": null
}

Rules:

- Only extract NEW information.
- Never regenerate old information.
- Never guess.
- Empty array if nothing new.
- Return JSON ONLY.
"""


def extract_memory(message: str):

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=f"{PROMPT}\n\nUser:\n{message}"
    )

    try:
        text = response.text.strip()

        if text.startswith("```json"):
            text = text.replace("```json", "").replace("```", "").strip()

        return json.loads(text)

    except Exception:
        return {
            "role": None,
            "companies_to_add": [],
            "interests_to_add": [],
            "briefing_time": None
        }