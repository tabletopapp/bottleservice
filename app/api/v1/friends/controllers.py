"""API Route handlers for friends."""

from fastapi import APIRouter, Depends, HTTPException, status

from app.api.v1.friends import services
from app.api.v1.friends.schemas import GetFriendsPayload
from app.database import db

router = APIRouter()


@router.get("/get_friends")
def get_friends(
    payload: GetFriendsPayload,
    session=Depends(db),
):
    try:
        results = services.get_friends(session, payload)
        return results
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error getting friends: {e}",
        )
