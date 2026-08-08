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
        .order("created_at")
        .execute()
    )


def remove_company(user_id, company):
    return (
        supabase
        .table("watchlists")
        .delete()
        .eq("user_id", user_id)
        .eq("company_name", company.title())
        .execute()
    )


def company_exists(user_id, company):
    return (
        supabase
        .table("watchlists")
        .select("id")
        .eq("user_id", user_id)
        .eq("company_name", company.title())
        .execute()
    )


def clear_watchlist(user_id):
    return (
        supabase
        .table("watchlists")
        .delete()
        .eq("user_id", user_id)
        .execute()
    )