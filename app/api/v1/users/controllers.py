"""API Route handlers for user."""

from fastapi import APIRouter, Depends

from app.database import db

router = APIRouter()


@router.post("/get_user")
def get_user(session=Depends(db)):
    return "Hello, World!"
