from app.scheduler.telegram_sender import send_main_menu


CHAT_ID = 6587173346  # replace with your Telegram chat ID


send_main_menu(CHAT_ID)

print("STATUS: MENU SENT")