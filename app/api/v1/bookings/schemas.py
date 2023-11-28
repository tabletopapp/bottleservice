"""Schemas for bookings."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CreateBookingPayload(BaseModel):
    guest_id: int
    table_id: int
    booking_datetime: str
    num_guests: Optional[int] = None
    # promoter_id: int


class BookingSchema(BaseModel):
    id: int
    guest_id: int
    table_id: int
    booking_datetime: datetime
    num_guests: Optional[int] = None
    # promoter_id: int
    is_active: bool = True

    class Config:
        from_attributes = True


class GetBookingsPayload(BaseModel):
    guest_id: int
