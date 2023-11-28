"""API Route handlers for tables."""

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from app.api.v1.tables import services
from app.api.v1.tables.schemas import GetTablesPayload, TableSchema
from app.database import db

router = APIRouter()


@router.get("/get_tables", response_model=List[TableSchema])
def get_tables(payload: GetTablesPayload, session=Depends(db)):
    try:
        results = services.get_tables(session, payload)
        return results
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error getting tables: {e}",
        )
