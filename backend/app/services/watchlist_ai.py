import re


def detect_watchlist_intent(message: str):

    text = message.lower().strip()

    # ---------- Add ----------
    add_patterns = [
        r"add (.+)",
        r"track (.+)",
        r"follow (.+)",
        r"watch (.+)"
    ]

    for pattern in add_patterns:
        match = re.search(pattern, text)
        if match:
            return {
                "intent": "add",
                "company": match.group(1).strip()
            }

    # ---------- Remove ----------
    remove_patterns = [
        r"remove (.+)",
        r"delete (.+)",
        r"untrack (.+)"
    ]

    for pattern in remove_patterns:
        match = re.search(pattern, text)
        if match:
            return {
                "intent": "remove",
                "company": match.group(1).strip()
            }

    # ---------- Show ----------
    if any(x in text for x in [
        "watchlist",
        "my stocks",
        "tracked companies"
    ]):
        return {
            "intent": "show"
        }

    return None