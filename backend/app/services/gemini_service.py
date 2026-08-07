from google import genai

from app.config.settings import (
    GEMINI_API_KEY,
    GEMINI_MODEL
)

from app.prompts.prompt_manager import build_prompt

client = genai.Client(
    api_key=GEMINI_API_KEY
)


def generate_response(message, history, memory):

    prompt = build_prompt(
        message,
        history,
        memory
    )

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt
    )

    return response.text