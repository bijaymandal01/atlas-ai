from fastapi import APIRouter

from app.models.research import (
    ResearchRequest,
    ResearchResponse,
)

from app.services.research_service import research_company

router = APIRouter(
    prefix="/research",
    tags=["Research"]
)


@router.post(
    "",
    response_model=ResearchResponse
)
def research(request: ResearchRequest):
    return research_company(request.company)