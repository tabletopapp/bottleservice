"""Schemas for clubs."""

from datetime import time
from typing import Optional

from pydantic import BaseModel


class ClubSchema(BaseModel):
    id: int
    name: str
    address_line_1: str
    address_line_2: Optional[str]
    city: str
    state: str
    zip_code: str
    phone_number: Optional[str]
    is_active: bool = True
    pricing_tier: Optional[int] = None
    opening_time: Optional[time] = None
    closing_time: Optional[time] = None
    banner_image_url: Optional[str] = None
    open_now: Optional[bool] = None

    class Config:
        from_attributes = True


class GetClubsPayload(BaseModel):
    club_name: Optional[str] = None
    party_size: Optional[int] = None
    budget_in_usd_cents: Optional[int] = None
    date: Optional[str] = None
    city: Optional[str] = None
