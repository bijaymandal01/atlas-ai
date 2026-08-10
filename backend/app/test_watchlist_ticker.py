from app.database.user_service import get_user
from app.database.watchlist_service import (
    get_watchlist,
    clear_watchlist,
)

from app.services.watchlist_service import (
    handle_watchlist_command,
)


TEST_USER_ID = "a13210fe-360e-4e40-8d40-4509bd590719"


clear_watchlist(TEST_USER_ID)

tests = [
    "Add Microsoft",
    "Add Apple",
    "Add Tesla",
]

for message in tests:

    print("=" * 60)
    print("USER:")
    print(message)

    reply = handle_watchlist_command(
        TEST_USER_ID,
        message
    )

    print("\nATLAS:")
    print(reply)


print("\n" + "=" * 60)
print("FINAL DATABASE WATCHLIST")
print("=" * 60)

watchlist = get_watchlist(TEST_USER_ID)

for item in watchlist.data:
    print(
        item["company_name"],
        "→",
        item["ticker"]
    )