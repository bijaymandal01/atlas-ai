from app.database.user_scheduler_service import (
    get_all_users,
)

from app.scheduler.telegram_sender import (
    send_telegram_message,
)

from app.services.morning_service import (
    generate_morning_brief,
)


def run_morning_job():

    users = get_all_users()

    for user in users.data:

        telegram_id = user["telegram_user_id"]

        try:

            report = generate_morning_brief(
                telegram_id
            )

            send_telegram_message(
                telegram_id,
                report,
            )

            print(
                f"Morning Brief sent to {telegram_id}"
            )

        except Exception as e:

            print(
                f"Failed for {telegram_id}: {e}"
            )