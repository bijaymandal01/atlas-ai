from app.database.user_service import (
    get_user,
    delete_user,
)

TEST_TELEGRAM_ID = 9999999999

# Find test user
user = get_user(TEST_TELEGRAM_ID)

if not user.data:
    print("TEST USER NOT FOUND")
    exit()

user_id = user.data[0]["id"]

# Delete test user
result = delete_user(user_id)

print("DELETE USER RESULT:")
print(result.data)

# Verify deletion
deleted_user = get_user(TEST_TELEGRAM_ID)

print("\nVERIFY DELETION:")
print(deleted_user.data)