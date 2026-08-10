from app.database.user_service import (
    create_user,
    get_user,
    delete_user,
)

from app.database.memory_service import (
    save_memory,
    get_user_memory,
)

from app.services.chat_service import chat


TEST_TELEGRAM_ID = 9999999998


# ==================================================
# 1. CLEAN TEST USER
# ==================================================

existing = get_user(TEST_TELEGRAM_ID)

if existing.data:

    delete_user(
        existing.data[0]["id"]
    )

# ==================================================
# 2. CREATE TEST USER
# ==================================================

created = create_user({
    "telegram_user_id": TEST_TELEGRAM_ID,
    "username": "memory_test",
    "full_name": "Memory Test User",
})

user_id = created.data[0]["id"]

print("TEST USER CREATED:")
print(user_id)


# ==================================================
# 3. PREPARE COMPLETED ONBOARDING
# ==================================================

save_memory(
    user_id,
    "role",
    '"Investor"'
)

save_memory(
    user_id,
    "market",
    '"US Stocks"'
)

save_memory(
    user_id,
    "watchlist",
    '["Apple", "Microsoft"]'
)

save_memory(
    user_id,
    "briefing_time",
    '"8:00 AM"'
)


print("\nONBOARDING MEMORY CREATED")


# ==================================================
# 4. CHECK MEMORY
# ==================================================

memory = get_user_memory(user_id)

print("\nCURRENT MEMORY:")
print(memory)


# ==================================================
# 5. NORMAL AI CHAT
# ==================================================

print("\n" + "=" * 70)
print("CHAT TEST")
print("=" * 70)

response = chat(
    TEST_TELEGRAM_ID,
    "I am interested in artificial intelligence companies."
)

print("\nATLAS RESPONSE:")
print(response)


# ==================================================
# 6. CHECK MEMORY AFTER CHAT
# ==================================================

updated_memory = get_user_memory(user_id)

print("\n" + "=" * 70)
print("MEMORY AFTER CHAT")
print("=" * 70)

print(updated_memory)