from fastapi import APIRouter

from app.scheduler.morning_job import run_morning_job
from app.scheduler.evening_job import run_evening_job

router = APIRouter(
    prefix="/jobs",
    tags=["Scheduler"]
)


@router.post("/morning")
def morning_job():

    run_morning_job()

    return {
        "success": True,
        "message": "Morning Brief Sent"
    }


@router.post("/evening")
def evening_job():

    run_evening_job()

    return {
        "success": True,
        "message": "Evening Wrap Sent"
    }