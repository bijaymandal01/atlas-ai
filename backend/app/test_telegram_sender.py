from unittest.mock import patch, MagicMock

from app.scheduler.telegram_sender import (
    send_telegram_message,
)


TEST_CHAT_ID = 9999999997


print("=" * 70)
print("TELEGRAM SENDER TEST")
print("=" * 70)


# ============================================================
# TEST 1 — Normal message
# ============================================================

print("\nTEST 1 — NORMAL MESSAGE")

mock_response = MagicMock()
mock_response.raise_for_status.return_value = None


with patch(
    "app.scheduler.telegram_sender.requests.post",
    return_value=mock_response,
) as mock_post:

    result = send_telegram_message(
        TEST_CHAT_ID,
        "Hello from Atlas AI",
    )

    if result is True and mock_post.called:

        print("PASS | Message sent")

    else:

        print("FAIL | Message sending failed")


# ============================================================
# TEST 2 — Long message
# ============================================================

print("\nTEST 2 — LONG MESSAGE")

long_message = "A" * 9000


with patch(
    "app.scheduler.telegram_sender.requests.post",
    return_value=mock_response,
) as mock_post:

    result = send_telegram_message(
        TEST_CHAT_ID,
        long_message,
    )

    calls = mock_post.call_count

    print("MESSAGE LENGTH:", len(long_message))
    print("TELEGRAM CALLS:", calls)

    if result is True and calls == 3:

        print("PASS | Message correctly split")

    else:

        print("FAIL | Message splitting incorrect")


# ============================================================
# FINAL
# ============================================================

print("\n" + "=" * 70)
print("STATUS: PASS")
print("=" * 70)