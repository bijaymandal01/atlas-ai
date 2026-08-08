from fastapi import APIRouter, Header, HTTPException

from app.config.settings import SCHEDULER_SECRET

from app.scheduler.morning_job import run_morning_job
from app.scheduler.evening_job import run_evening_job

router = APIRouter(
    prefix="/jobs",
    tags=["Scheduler"]
)


def verify_scheduler(secret: str):

    if secret != SCHEDULER_SECRET:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )


@router.post("/morning")
def morning_job(
    x_scheduler_key: str = Header(...)
):

    verify_scheduler(x_scheduler_key)

    run_morning_job()

    return {
        "success": True,
        "message": "Morning Brief Sent"
    }


@router.post("/evening")
def evening_job(
    x_scheduler_key: str = Header(...)
):

    verify_scheduler(x_scheduler_key)

    run_evening_job()

    return {
        "success": True,
        "message": "Evening Wrap Sent"
    }
