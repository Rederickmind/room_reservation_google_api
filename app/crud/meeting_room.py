# app/crud/meeting_room.py
from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.meeting_room import MeetingRoom


# Создаем новый класс, унаследованный от CRUDBase.
class CRUDMeetingRoom(CRUDBase):

    # Преобразуем функцию в метод класса.
    async def get_room_id_by_name(
            # Дописываем параметр self.
            # В качестве альтернативы здесь можно
            # применить декоратор @staticmethod.
            self,
            room_name: str,
            session: AsyncSession,
    ) -> Optional[int]:
        db_room_id = await session.execute(
            select(MeetingRoom.id).where(
                MeetingRoom.name == room_name
            )
        )
        db_room_id = db_room_id.scalars().first()
        return db_room_id


# Объект crud наследуем уже не от CRUDBase,
# а от только что созданного класса CRUDMeetingRoom.
# Для инициализации передаем модель, как и в CRUDBase.
meeting_room_crud = CRUDMeetingRoom(MeetingRoom)
