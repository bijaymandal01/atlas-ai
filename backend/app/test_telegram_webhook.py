from unittest.mock import patch

from app.main import app
from fastapi.testclient import TestClient


client = TestClient(app)


TEST_TELEGRAM_ID = 9999999997


print("=" * 70)
print("TELEGRAM WEBHOOK TEST")
print("=" * 70)


update = {

    "update_id": 10001,

    "message": {

        "message_id": 1,

        "from": {
            "id": TEST_TELEGRAM_ID,
            "is_bot": False,
            "first_name": "Test",
        },

        "chat": {
            "id": TEST_TELEGRAM_ID,
            "type": "private",
        },

        "text": "Show my watchlist",
    },
}


with patch(
    "app.api.telegram.send_telegram_message"
) as mock_send:

    response = client.post(
        "/telegram/webhook",
        json=update,
    )


print("\nHTTP STATUS:")
print(response.status_code)

print("\nRESPONSE:")
print(response.json())

print("\nTELEGRAM SEND CALLED:")
print(mock_send.called)


if response.status_code == 200:
    print("\nPASS | Webhook returned HTTP 200")
else:
    print("\nFAIL | Webhook failed")


if response.json().get("ok") is True:
    print("PASS | Telegram webhook returned ok=True")
else:
    print("FAIL | Webhook response incorrect")


if mock_send.called:
    print("PASS | Telegram response function called")
else:
    print("FAIL | Telegram response function not called")


print("\n" + "=" * 70)