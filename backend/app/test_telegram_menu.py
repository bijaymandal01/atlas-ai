from app.scheduler.telegram_sender import send_telegram_message

CHAT_ID = 6587173346

send_telegram_message(
    CHAT_ID,
    "🤖 Atlas AI menu test"
)

print("STATUS: MENU SENT")