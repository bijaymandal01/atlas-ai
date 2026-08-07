from app.database.supabase import supabase


def save_decision(data):
    return (
        supabase
        .table("decision_journal")
        .insert(data)
        .execute()
    )


def get_decisions(user_id):
    return (
        supabase
        .table("decision_journal")
        .select("*")
        .eq("user_id", user_id)
        .execute()
    )