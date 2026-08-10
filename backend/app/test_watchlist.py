from app.database.user_service import (
    create_user,
    get_user,
    delete_user,
)

from app.database.watchlist_service import (
    add_company,
    get_watchlist,
)


USER_A = 9999999996
USER_B = 9999999995


# ==================================================
# CLEAN OLD TEST USERS
# ==================================================

for telegram_id in [USER_A, USER_B]:

    existing = get_user(telegram_id)

    if existing.data:
        delete_user(existing.data[0]["id"])


# ==================================================
# CREATE USER A
# ==================================================

user_a = create_user({
    "telegram_user_id": USER_A,
    "username": "watchlist_user_a",
    "full_name": "Watchlist User A",
})

user_a_id = user_a.data[0]["id"]


# ==================================================
# CREATE USER B
# ==================================================

user_b = create_user({
    "telegram_user_id": USER_B,
    "username": "watchlist_user_b",
    "full_name": "Watchlist User B",
})

user_b_id = user_b.data[0]["id"]


# ==================================================
# USER A → APPLE
# ==================================================

add_company({
    "user_id": user_a_id,
    "company_name": "Apple",
    "ticker": "APPLE",
})


# ==================================================
# USER B → MICROSOFT
# ==================================================

add_company({
    "user_id": user_b_id,
    "company_name": "Microsoft",
    "ticker": "MICROSOFT",
})


# ==================================================
# READ BOTH WATCHLISTS
# ==================================================

watchlist_a = get_watchlist(user_a_id)
watchlist_b = get_watchlist(user_b_id)


print("=" * 60)
print("USER A WATCHLIST:")
print(watchlist_a.data)

print("\nUSER B WATCHLIST:")
print(watchlist_b.data)


# ==================================================
# VERIFY ISOLATION
# ==================================================

a_companies = [
    item["company_name"]
    for item in watchlist_a.data
]

b_companies = [
    item["company_name"]
    for item in watchlist_b.data
]


print("\n" + "=" * 60)
print("ISOLATION TEST:")

if "Apple" in a_companies and "Microsoft" not in a_companies:
    print("USER A ISOLATION: PASS")
else:
    print("USER A ISOLATION: FAIL")


if "Microsoft" in b_companies and "Apple" not in b_companies:
    print("USER B ISOLATION: PASS")
else:
    print("USER B ISOLATION: FAIL")