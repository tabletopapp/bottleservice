"""Schemas for tables."""

from typing import Optional

from pydantic import BaseModel


class GetTablesPayload(BaseModel):
    club_id: int
    date: str
    party_size: Optional[int] = None


class TableSchema(BaseModel):
    id: int
    num_seats: int
    price_in_usd_cents: int
    tier: int
    name: str
    is_active: bool
    available: Optional[bool] = None

    class Config:
        from_attributes = True
