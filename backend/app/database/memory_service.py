import json

from app.database.supabase import supabase


def get_user_memory(user_id):

    response = (
        supabase
        .table("memory")
        .select("*")
        .eq("user_id", user_id)
        .execute()
    )

    memories = response.data

    for item in memories:

        try:
            item["memory_value"] = json.loads(item["memory_value"])
        except Exception:
            pass

    return memories


def get_memory_by_key(user_id, key):

    response = (
        supabase
        .table("memory")
        .select("*")
        .eq("user_id", user_id)
        .eq("memory_key", key)
        .execute()
    )

    if not response.data:
        return None

    row = response.data[0]

    try:
        row["memory_value"] = json.loads(row["memory_value"])
    except Exception:
        pass

    return row


def save_memory(user_id, key, value):

    existing = get_memory_by_key(user_id, key)

    if existing:

        return (
            supabase
            .table("memory")
            .update({
                "memory_value": value
            })
            .eq("id", existing["id"])
            .execute()
        )

    return (
        supabase
        .table("memory")
        .insert({
            "user_id": user_id,
            "memory_key": key,
            "memory_value": value
        })
        .execute()
    )