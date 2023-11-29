"""Services for clubs."""

from typing import List

from sqlalchemy.orm import Session

from app.api.v1.clubs.models import Club
from app.api.v1.clubs.schemas import ClubSchema, GetClubsPayload
from app.api.v1.tables.models import Table


def get_clubs(session: Session, payload: GetClubsPayload) -> List[ClubSchema]:
    query = (
        session.query(Club)
        .join(Table, Table.club_id == Club.id)
        .filter(Club.is_active == True)
    )

    if payload.club_name:
        query = query.filter(Club.name.ilike(f"%{payload.club_name}%"))

    if payload.party_size:
        query = query.filter(Table.num_seats >= payload.party_size)

    if payload.budget_in_usd_cents:
        query = query.filter(Table.price_in_usd_cents <= payload.budget_in_usd_cents)

    if payload.location:
        query = query.filter(Club.city.ilike(f"%{payload.location}%"))

    results: List[Club] = query.all()
    schema_results: List[ClubSchema] = [
        ClubSchema.model_validate(club) for club in results
    ]
    return list(set(schema_results))
