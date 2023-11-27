"""Schemas for clubs."""

from pydantic import BaseModel


class ClubSchema(BaseModel):
    id: int
    name: str
    address_line_1: str
    address_line_2: str
    city: str
    state: str
    zip_code: str
    phone_number: str
    is_active: bool

    class Config:
        orm_mode = True


class GetClubsPayload(BaseModel):
    club_name: str = None
    party_size: int = None
    budget_in_usd_cents: int = None
    date: str = None
    location: str = None
