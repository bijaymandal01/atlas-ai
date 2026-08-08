from pydantic import BaseModel


class AddCompanyRequest(BaseModel):
    telegram_user_id: int
    company: str


class RemoveCompanyRequest(BaseModel):
    telegram_user_id: int
    company: str


class WatchlistResponse(BaseModel):
    watchlist: list[str]