from app.database.supabase import supabase


def save_message(user_id: str, sender: str, message: str):

    return (
        supabase
        .table("conversations")
        .insert({
            "user_id": user_id,
            "sender": sender,
            "message": message
        })
        .execute()
    )


def get_recent_messages(user_id: str, limit: int = 10):

    response = (
        supabase
        .table("conversations")
        .select("*")
        .eq("user_id", user_id)
        .order("created_at", desc=True)
        .limit(limit)
        .execute()
    )

    return response.data