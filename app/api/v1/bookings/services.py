"""Services for bookings."""

from datetime import datetime
from typing import List

from sqlalchemy.orm import Session

from app.api.v1.bookings.models import Booking
from app.api.v1.bookings.schemas import (
    BookingSchema,
    CreateBookingPayload,
    GetBookingsPayload,
)


def create_booking(session: Session, payload: CreateBookingPayload) -> int:
    booking_datetime = datetime.strptime(payload.booking_datetime, "%Y-%m-%d %H:%M:%S")

    booking = Booking(
        guest_id=payload.guest_id,
        table_id=payload.table_id,
        booking_datetime=booking_datetime,
    )
    session.add(booking)
    session.commit()
    return booking.id


def get_previous_bookings(
    session: Session,
    payload: GetBookingsPayload,
) -> List[BookingSchema]:
    query = (
        session.query(Booking)
        .filter(Booking.is_active == True)
        .filter(Booking.booking_datetime < datetime.now())
        .filter(Booking.guest_id == payload.guest_id)
    )
    results: List[Booking] = query.all()
    schema_results: List[BookingSchema] = [
        BookingSchema.model_validate(booking) for booking in results
    ]
    return schema_results


def get_upcoming_bookings(
    session: Session,
    payload: GetBookingsPayload,
) -> List[BookingSchema]:
    query = (
        session.query(Booking)
        .filter(Booking.is_active == True)
        .filter(Booking.booking_datetime >= datetime.now())
        .filter(Booking.guest_id == payload.guest_id)
    )
    results: List[Booking] = query.all()
    schema_results: List[BookingSchema] = [
        BookingSchema.model_validate(booking) for booking in results
    ]
    return schema_results
