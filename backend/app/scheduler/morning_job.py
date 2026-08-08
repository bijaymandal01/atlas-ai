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

    print("=" * 60)
    print("🌅 MORNING JOB STARTED")
    print("=" * 60)

    users = get_all_users()

    total = len(users.data)
    success = 0
    failed = 0

    print(f"Total Users : {total}")

    for user in users.data:

        telegram_id = user["telegram_user_id"]

        print(f"\nProcessing User : {telegram_id}")

        try:

            report = generate_morning_brief(
                telegram_id
            )

            send_telegram_message(
                telegram_id,
                report,
            )

            success += 1

            print(
                f"✅ Morning Brief sent to {telegram_id}"
            )

        except Exception as e:

            failed += 1

            print(
                f"❌ Failed for {telegram_id}: {e}"
            )

            continue

    print("\n" + "=" * 60)
    print("🌅 MORNING JOB COMPLETED")
    print(f"Total Users : {total}")
    print(f"Successful : {success}")
    print(f"Failed : {failed}")
    print("=" * 60)