# app/api/endpoints/__init__.py
from .meeting_room import router as meeting_room_router # noqa
from .reservation import router as reservation_router # noqa
from .user import router as user_router # noqa
from .google_api import router as google_api_router # noqa