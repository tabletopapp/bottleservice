"""Schemas for bookings."""

from datetime import datetime, time
from typing import Optional

from pydantic import BaseModel


class CreateBookingPayload(BaseModel):
    guest_id: int
    table_id: int
    booking_datetime: str
    num_guests: Optional[int] = None
    # promoter_id: int


class BookingReturnPayload(BaseModel):
    booking_id: int
    table_owner_id: int
    table_id: int
    booking_datetime: datetime
    club_name: str
    banner_image_url: Optional[str] = None
    opening_time: time
    closing_time: time
    num_seats: Optional[int] = None
    address_line_1: str
    address_line_2: Optional[str] = None
    city: str
    state: str
    zip_code: str


class GetAllBookingsPayload(BaseModel):
    guest_id: int


class GetBookingsForDatePayload(BaseModel):
    guest_id: int
    date: str
