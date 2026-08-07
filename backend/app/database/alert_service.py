from app.database.supabase import supabase


def create_alert(data):
    return (
        supabase
        .table("alerts")
        .insert(data)
        .execute()
    )


def get_alerts(user_id):
    return (
        supabase
        .table("alerts")
        .select("*")
        .eq("user_id", user_id)
        .execute()
    )


def delete_alert(alert_id):
    return (
        supabase
        .table("alerts")
        .delete()
        .eq("id", alert_id)
        .execute()
    )