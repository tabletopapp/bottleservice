"""Services for friends."""


from typing import List

from sqlalchemy.orm import Session

from app.api.v1.friends.models import Friend
from app.api.v1.friends.schemas import FriendSchemaReturnPayload, GetFriendsPayload
from app.api.v1.guests.models import Guest
from app.api.v1.users.models import User


def get_friends(
    session: Session,
    payload: GetFriendsPayload,
) -> List[FriendSchemaReturnPayload]:
    query = (
        session.query(
            Guest.id.label("guest_id"),
            User.first_name.label("first_name"),
            User.last_name.label("last_name"),
        )
        .select_from(Friend)
        .join(Guest, Guest.id == Friend.addressee_guest_id)
        .join(User, User.id == Guest.user_id)
        .filter(
            Friend.requesting_guest_id == payload.requesting_guest_id,
        )
    )
    results = query.all()
    schema_results: List[FriendSchemaReturnPayload] = []
    for guest in results:
        print(guest)
        print(guest.guest_id)
        schema_results.append(
            FriendSchemaReturnPayload(
                guest_id=guest.guest_id,
                first_name=guest.first_name,
                last_name=guest.last_name,
            ),
        )

    return schema_results
