from app.database.user_scheduler_service import get_all_users

users = get_all_users()

for user in users.data:
    print(user)