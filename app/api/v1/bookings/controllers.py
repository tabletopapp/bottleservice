"""API Route handlers for bookings."""

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from app.api.v1.bookings import services
from app.api.v1.bookings.schemas import (
    BookingSchema,
    CreateBookingPayload,
    GetBookingsPayload,
)
from app.database import db

router = APIRouter()


@router.post("/create_booking")
def create_booking(payload: CreateBookingPayload, session=Depends(db)):
    try:
        booking_id = services.create_booking(session, payload)
        return booking_id
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating booking: {e}",
        )


@router.get("/get_previous_bookings", response_model=List[BookingSchema])
def get_previous_bookings(
    payload: GetBookingsPayload,
    session=Depends(db),
):
    try:
        results = services.get_previous_bookings(session, payload)
        return results
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error getting previous bookings: {e}",
        )


@router.get("/get_upcoming_bookings", response_model=List[BookingSchema])
def get_upcoming_bookings(
    payload: GetBookingsPayload,
    session=Depends(db),
):
    try:
        results = services.get_upcoming_bookings(session, payload)
        return results
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error getting upcoming bookings: {e}",
        )
