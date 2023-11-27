from fastapi import APIRouter

from app.api.v1.clubs.controllers import router as clubs_router
from app.api.v1.users.controllers import router as users_router

v1_router = APIRouter()

v1_router.include_router(
    users_router,
    prefix="/users",
    tags=["users"],
)

v1_router.include_router(
    clubs_router,
    prefix="/clubs",
    tags=["clubs"],
)
