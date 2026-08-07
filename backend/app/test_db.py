from app.database.user_service import create_user

response = create_user({
    "telegram_user_id": 123456789,
    "full_name": "Test User",
    "role": "Investor"
})

print(response.data)