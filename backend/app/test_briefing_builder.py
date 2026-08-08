from app.database.user_service import get_user
from app.database.watchlist_service import get_watchlist

from app.services.briefing_builder import (
    build_briefing_dashboard,
)

TELEGRAM_USER_ID = 123456789

user = get_user(TELEGRAM_USER_ID)

if not user.data:
    print("User not found")
    exit()

user_id = user.data[0]["id"]

watchlist = get_watchlist(user_id)

dashboard = build_briefing_dashboard(watchlist)

print(dashboard)