"""API Route handlers for clubs."""

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from app.api.v1.clubs import services
from app.api.v1.clubs.schemas import ClubSchema, GetClubsPayload
from app.database import db

router = APIRouter()


@router.post("/get_clubs", response_model=List[ClubSchema])
def get_clubs(
    payload: GetClubsPayload,
    session=Depends(db),
):
    try:
        results = services.get_clubs(session, payload)
        return results
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error getting clubs: {e}",
        )
