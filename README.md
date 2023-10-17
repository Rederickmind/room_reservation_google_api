## Приложение для Бронирования переговорок с интеграцией Google API для отчётов

### О проекте

Дописать


### Используемые технологии
- Python 3.9.10
- Alembic 1.7.7
- SQLalchemy 1.4.49
- SQLlite
- FastAPI 0.78.0
- FastAPI Users 10.0.6
- Uvicorn

### Установка и запуск

**Клонируйте репозиторий:**

```
git clone git@github.com:Rederickmind/room_reservation_google_api.git
```

**Установите и активируйте виртуальное окружение:**

```
python -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

**Обновите менеджер pip и установите зависимости**

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

### Необходимо заполнить env-файл для запуска
```
touch .env
```
```
# .env
APP_TITLE = Кошачий благотворительный фонд (QR Kot)
DESCRIPTION = Сервис для поддержки котов
DATABASE_URL = sqlite+aiosqlite:///./fastapi.db
SECRET = Секретное слово
FIRST_SUPERUSER_EMAIL = Е-мэил суперпользователя, который создастся при запуске приложения
FIRST_SUPERUSER_PASSWORD = Пароль суперпользователя, который создастся при запуске приложениял
```


### Необходимо инициализировать Alembic в проекте, создать и выполнить миграции:
- следует указать, что Alembic должен использовать асинхронный шаблон --template async (или короткая форма -t async)
```
alembic init --template async alembic
```
- Генерация миграций
```
alembic revision --autogenerate -m "First migration"
```
- Применение миграций
```
alembic upgrade head
```
Если что-то пошло не так — можно отменить миграции: одну, несколько или вообще все.
Чтобы отменить все миграции, которые были в проекте, используется команда:
```
alembic downgrade base 
```

### Запуск проекта:
```
uvicorn app.main:app --reload
```

- После запуска проект будет доступен по адресу: http://127.0.0.1:8000
- http://127.0.0.1:8000/docs - автоматически сгенерированная документация Swagger
- http://127.0.0.1:8000/redoc - автоматически сгенерированная документация ReDoc