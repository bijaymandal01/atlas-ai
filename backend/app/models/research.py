from pydantic import BaseModel


class ResearchRequest(BaseModel):
    company: str


class ResearchResponse(BaseModel):
    company: dict
    price: dict
    report: str