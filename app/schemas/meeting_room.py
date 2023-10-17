# app/schemas/meeting_room.py

from typing import Optional

from pydantic import BaseModel, Field, validator


# Базовый класс схемы, от которого наследуем все остальные.
class MeetingRoomBase(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str]


# Теперь наследуем схему не от BaseModel, а от MeetingRoomBase.
class MeetingRoomCreate(MeetingRoomBase):
    # Переопределяем атрибут name, делаем его обязательным.
    name: str = Field(..., min_length=1, max_length=100)
    # Описывать поле description не нужно: оно уже есть в базовом классе.

    class Config:
        @validator('name')
        def name_cant_be_empty(cls, value: str):
            if value == '' or value is None:
                raise ValueError('Cтрока не должна быть пустой')
            # Если проверка пройдена, возвращаем значение поля.
            return value


# Новый класс для обновления объектов.
class MeetingRoomUpdate(MeetingRoomBase):
    pass

    @validator('name')
    def name_cannot_be_null(cls, value):
        if value is None:
            raise ValueError('Имя переговорки не может быть пустым!')
        return value


# Возвращаемую схему унаследуем от MeetingRoomCreate,
# чтобы снова не описывать обязательное поле name.
class MeetingRoomDB(MeetingRoomCreate):
    id: int

    class Config:
        # Нужно указать, что схема может принимать на вход объект базы данных,
        # а не только Python-словарь или JSON-объект.
        orm_mode = True
