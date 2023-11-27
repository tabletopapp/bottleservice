"""API Route handlers for tables."""

from fastapi import APIRouter, Depends

from app.database import db

router = APIRouter()


@router.post("/stub")
def stub(session=Depends(db)):
    """Write documentation here."""
