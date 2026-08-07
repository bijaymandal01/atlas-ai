from app.database.supabase import supabase


def add_company(data):
    return (
        supabase
        .table("watchlists")
        .insert(data)
        .execute()
    )


def get_watchlist(user_id):
    return (
        supabase
        .table("watchlists")
        .select("*")
        .eq("user_id", user_id)
        .execute()
    )


def remove_company(company_id):
    return (
        supabase
        .table("watchlists")
        .delete()
        .eq("id", company_id)
        .execute()
    )