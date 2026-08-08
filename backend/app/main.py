from fastapi import FastAPI

from app.api.chat import router as chat_router
from app.api.research import router as research_router
from app.api.watchlist import router as watchlist_router
from app.api.jobs import router as jobs_router

app = FastAPI(title="Atlas AI")

app.include_router(chat_router)
app.include_router(research_router)
app.include_router(watchlist_router)
app.include_router(jobs_router)