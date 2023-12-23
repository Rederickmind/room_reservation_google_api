from fastapi import APIRouter

from app.api.endpoints import (
    google_api_router, meeting_room_router, reservation_router, user_router
)

main_router = APIRouter()
main_router.include_router(
    meeting_room_router, prefix='/meeting_rooms', tags=['Meeting Rooms']
)
main_router.include_router(
    reservation_router, prefix='/reservations', tags=['Reservations']
)
main_router.include_router(
    google_api_router, prefix='/google', tags=['Google']
)
main_router.include_router(user_router)
