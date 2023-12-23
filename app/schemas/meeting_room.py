from typing import Optional

from pydantic import BaseModel, Field, validator


class MeetingRoomBase(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str]


class MeetingRoomCreate(MeetingRoomBase):
    name: str = Field(..., min_length=1, max_length=100)

    class Config:
        @validator('name')
        def name_cant_be_empty(cls, value: str):
            if value == '' or value is None:
                raise ValueError('Cтрока не должна быть пустой')
            # Если проверка пройдена, возвращаем значение поля.
            return value


class MeetingRoomUpdate(MeetingRoomBase):
    pass

    @validator('name')
    def name_cannot_be_null(cls, value):
        if value is None:
            raise ValueError('Имя переговорки не может быть пустым!')
        return value


class MeetingRoomDB(MeetingRoomCreate):
    id: int

    class Config:
        orm_mode = True
