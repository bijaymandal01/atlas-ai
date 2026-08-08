from app.database.supabase import supabase


def get_all_users():

    return (
        supabase.table("users")
        .select("*")
        .execute()
    )