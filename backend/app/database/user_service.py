from app.database.supabase import supabase


def create_user(data: dict):
    return (
        supabase
        .table("users")
        .insert(data)
        .execute()
    )


def get_user(telegram_user_id: int):
    return (
        supabase
        .table("users")
        .select("*")
        .eq("telegram_user_id", telegram_user_id)
        .execute()
    )


def update_user(user_id: str, data: dict):
    return (
        supabase
        .table("users")
        .update(data)
        .eq("id", user_id)
        .execute()
    )


def delete_user(user_id: str):
    return (
        supabase
        .table("users")
        .delete()
        .eq("id", user_id)
        .execute()
    )