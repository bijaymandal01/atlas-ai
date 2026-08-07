from app.prompts.system_prompt import SYSTEM_PROMPT


def build_prompt(message, history, memory):
    prompt = SYSTEM_PROMPT

    # -------------------------
    # User Memory
    # -------------------------
    prompt += "\n\n=== USER MEMORY ===\n"

    if memory:
        for item in memory:
            prompt += (
                f"{item['memory_key']}: "
                f"{item['memory_value']}\n"
            )
    else:
        prompt += "No stored memory.\n"

    # -------------------------
    # Conversation History
    # -------------------------
    prompt += "\n=== RECENT CONVERSATION ===\n"

    if history:
        for chat in reversed(history):
            prompt += (
                f"{chat['sender']}: "
                f"{chat['message']}\n"
            )
    else:
        prompt += "No previous conversation.\n"

    # -------------------------
    # Current User Message
    # -------------------------
    prompt += f"\nUser: {message}\n"
    prompt += "Assistant:"

    return prompt