"""Services for bookings."""

from datetime import datetime
from typing import List

from sqlalchemy import Date, cast
from sqlalchemy.orm import Session

from app.api.v1.bookings.models import Booking
from app.api.v1.bookings.schemas import BookingReturnPayload, CreateBookingPayload
from app.api.v1.clubs.models import Club
from app.api.v1.tables.models import Table


def create_booking(session: Session, payload: CreateBookingPayload) -> int:
    booking_datetime = datetime.strptime(payload.booking_datetime, "%Y-%m-%dT%H:%M:%S")

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
    guest_id: int,
) -> List[BookingReturnPayload]:
    query = (
        session.query(
            Booking.id.label("booking_id"),
            Booking.guest_id.label("guest_id"),
            Booking.table_id.label("table_id"),
            Booking.booking_datetime.label("booking_datetime"),
            Club.name.label("club_name"),
            Club.opening_time.label("opening_time"),
            Club.closing_time.label("closing_time"),
            Club.banner_image_url.label("banner_image_url"),
            Club.address_line_1.label("address_line_1"),
            Club.address_line_2.label("address_line_2"),
            Club.city.label("city"),
            Club.state.label("state"),
            Club.zip_code.label("zip_code"),
            Table.num_seats.label("num_seats"),
        )
        .select_from(Booking)
        .join(Table, Table.id == Booking.table_id)
        .join(Club, Club.id == Table.club_id)
        .filter(Booking.is_active == True)
        .filter(Booking.booking_datetime < datetime.now())
        .filter(Booking.guest_id == guest_id)
    )
    results = query.all()

    return_values: List[BookingReturnPayload] = []
    for result in results:
        return_values.append(
            BookingReturnPayload(
                booking_id=result.booking_id,
                table_owner_id=result.guest_id,
                table_id=result.table_id,
                booking_datetime=result.booking_datetime,
                club_name=result.club_name,
                banner_image_url=result.banner_image_url,
                opening_time=result.opening_time,
                closing_time=result.closing_time,
                num_seats=result.num_seats,
                address_line_1=result.address_line_1,
                address_line_2=result.address_line_2,
                city=result.city,
                state=result.state,
                zip_code=result.zip_code,
            ),
        )

    return return_values


def get_upcoming_bookings(
    session: Session,
    guest_id: int,
) -> List[BookingReturnPayload]:
    query = (
        session.query(
            Booking.id.label("booking_id"),
            Booking.guest_id.label("guest_id"),
            Booking.table_id.label("table_id"),
            Booking.booking_datetime.label("booking_datetime"),
            Club.name.label("club_name"),
            Club.banner_image_url.label("banner_image_url"),
            Club.opening_time.label("opening_time"),
            Club.closing_time.label("closing_time"),
            Club.address_line_1.label("address_line_1"),
            Club.address_line_2.label("address_line_2"),
            Club.city.label("city"),
            Club.state.label("state"),
            Club.zip_code.label("zip_code"),
            Table.num_seats.label("num_seats"),
        )
        .select_from(Booking)
        .join(Table, Table.id == Booking.table_id)
        .join(Club, Club.id == Table.club_id)
        .filter(Booking.is_active == True)
        .filter(Booking.booking_datetime >= datetime.now())
        .filter(Booking.guest_id == guest_id)
    )
    results = query.all()

    return_values: List[BookingReturnPayload] = []
    for result in results:
        return_values.append(
            BookingReturnPayload(
                booking_id=result.booking_id,
                table_owner_id=result.guest_id,
                table_id=result.table_id,
                booking_datetime=result.booking_datetime,
                club_name=result.club_name,
                banner_image_url=result.banner_image_url,
                opening_time=result.opening_time,
                closing_time=result.closing_time,
                num_seats=result.num_seats,
                address_line_1=result.address_line_1,
                address_line_2=result.address_line_2,
                city=result.city,
                state=result.state,
                zip_code=result.zip_code,
            ),
        )
    return return_values


def get_bookings_for_table_on_date(
    session: Session,
    table_id: int,
    date: str,  # YYYY-MM-DD
) -> List[Booking]:
    booking_date = datetime.strptime(date, "%Y-%m-%d")
    query = (
        session.query(Booking)
        .filter(Booking.is_active == True)
        .filter(cast(Booking.booking_datetime, Date) == booking_date)
        .filter(Booking.table_id == table_id)
    )
    results: List[Booking] = query.all()
    return results
