from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship
from app.core.db import Base


class MeetingRoom(Base):
    # Имя переговорки должно быть не больше 100 символов,
    # уникальным и непустым.
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text)
    # Связь между моделями через функцию relationship.
    reservations = relationship('Reservation', cascade='delete')
