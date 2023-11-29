"""Services for clubs."""

from datetime import datetime
from typing import List

import pytz
from sqlalchemy.orm import Session

from app.api.v1.clubs.models import Club
from app.api.v1.clubs.schemas import ClubSchema, GetClubsPayload
from app.api.v1.tables.models import Table


def get_clubs(session: Session, payload: GetClubsPayload) -> List[ClubSchema]:
    query = (
        session.query(
            Club,
        )
        .join(Table, Table.club_id == Club.id)
        .filter(Club.is_active == True)
    )

    if payload.club_name:
        query = query.filter(Club.name.ilike(f"%{payload.club_name}%"))

    if payload.party_size:
        query = query.filter(Table.num_seats >= payload.party_size)

    if payload.budget_in_usd_cents:
        query = query.filter(Table.price_in_usd_cents <= payload.budget_in_usd_cents)

    if payload.city:
        query = query.filter(Club.city.ilike(f"%{payload.city}%"))

    results: List[Club] = query.all()
    schema_results: List[ClubSchema] = [
        ClubSchema.model_validate(club) for club in results
    ]

    LA_timezone = pytz.timezone("America/Los_Angeles")
    LA_time = datetime.now(LA_timezone)

    for club in schema_results:
        opening_time = LA_time.replace(
            hour=club.opening_time.hour,
            minute=club.opening_time.minute,
            second=club.opening_time.second,
        )
        closing_time = LA_time.replace(
            day=LA_time.day + 1,
            hour=club.closing_time.hour,
            minute=club.closing_time.minute,
            second=club.closing_time.second,
        )
        if opening_time < LA_time < closing_time:
            club.open_now = True
        else:
            club.open_now = False

    return schema_results
