"""Services for tables."""
from typing import List

from sqlalchemy.orm import Session

from app.api.v1.bookings import services as booking_services
from app.api.v1.bookings.models import Booking
from app.api.v1.tables.models import Table
from app.api.v1.tables.schemas import GetTablesPayload, TableSchema


def get_tables(session: Session, payload: GetTablesPayload) -> List[TableSchema]:
    query = (
        session.query(Table)
        .filter(Table.is_active == True)
        .filter(Table.club_id == payload.club_id)
    )

    if payload.party_size:
        query = query.filter(Table.num_seats >= payload.party_size)

    results: List[Table] = query.all()
    schema_results: List[TableSchema] = [
        TableSchema.model_validate(table) for table in results
    ]

    for result in schema_results:
        bookings: List[Booking] = booking_services.get_bookings_for_table_on_date(
            session,
            result.id,
            payload.date,
        )
        if len(bookings) >= result.max_num_tables:
            result.available = False
        else:
            result.available = True

    return schema_results
