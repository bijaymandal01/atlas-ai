from fastapi import APIRouter, HTTPException

from app.models.watchlist import (
    AddCompanyRequest,
    RemoveCompanyRequest,
    WatchlistResponse,
)

from app.database.user_service import get_user

from app.database.watchlist_service import (
    add_company,
    get_watchlist,
    remove_company,
    company_exists,
    clear_watchlist,
)

router = APIRouter(
    prefix="/watchlist",
    tags=["Watchlist"],
)


@router.post("/add")
def add(request: AddCompanyRequest):

    user = get_user(request.telegram_user_id)

    if not user.data:
        raise HTTPException(status_code=404, detail="User not found")

    user_id = user.data[0]["id"]

    exists = company_exists(user_id, request.company)

    if exists.data:
        return {
            "message": f"{request.company} already exists in watchlist."
        }

    add_company({
        "user_id": user_id,
        "company_name": request.company.title(),
        "ticker": request.company.upper(),
    })

    return {
        "message": f"{request.company.title()} added successfully."
    }


@router.get("/{telegram_user_id}", response_model=WatchlistResponse)
def watchlist(telegram_user_id: int):

    user = get_user(telegram_user_id)

    if not user.data:
        raise HTTPException(status_code=404, detail="User not found")

    user_id = user.data[0]["id"]

    data = get_watchlist(user_id)

    companies = [
        company["company_name"]
        for company in data.data
    ]

    return {
        "watchlist": companies
    }


@router.post("/remove")
def remove(request: RemoveCompanyRequest):

    user = get_user(request.telegram_user_id)

    if not user.data:
        raise HTTPException(status_code=404, detail="User not found")

    user_id = user.data[0]["id"]

    exists = company_exists(user_id, request.company)

    if not exists.data:
        return {
            "message": f"{request.company.title()} is not in your watchlist."
        }

    remove_company(
        user_id,
        request.company
    )

    return {
        "message": f"{request.company.title()} removed successfully."
    }


@router.delete("/{telegram_user_id}")
def clear(telegram_user_id: int):

    user = get_user(telegram_user_id)

    if not user.data:
        raise HTTPException(status_code=404, detail="User not found")

    user_id = user.data[0]["id"]

    clear_watchlist(user_id)

    return {
        "message": "Watchlist cleared successfully."
    }