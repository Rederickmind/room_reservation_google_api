## Приложение для Бронирования переговорок с интеграцией Google API для отчётов

### О проекте

Приложение позволяет создавать переговорные комнаты в системе и бронировать их на определенное время.
Пользователь может зарегистрироваться в системе и забронировать комнату или удалить свою бронь, а суперюзер обладает возможностями добавления/удаления и изменения комнат, удалять чужие бронирования, а также выгрузить отчет о частоте бронирования комнат в заданный период времени средствами Google Sheets.


### Используемые технологии
- Python 3.9.10
- Alembic 1.7.7
- SQLalchemy 1.4.49
- SQLlite
- FastAPI 0.78.0
- FastAPI Users 10.0.6
- Uvicorn

### Полезные ссылки
- Консоль Google Cloud Platform https://console.cloud.google.com/projectselector2/home/dashboard?pli=1
- Google Cloud Platform - настройка API и получение ключей https://docs.google.com/document/d/1SWn7jXcjgNQAjnktgsbKEhSZtO-hbzM7-vZ9mwXojug/edit?usp=sharing

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

### Необходимо заполнить env-файл для запуска (переписать)
```
touch .env
```
```
# .env
APP_TITLE = Сервис бронирования переговорных комнат
DESCRIPTION = Возможность бронировать помещения на определённый период времени. При этом приложение должно проверять, не забронировал ли уже кто-то это помещение и свободно ли всё время, на которое бронируется эта переговорка.
DATABASE_URL = sqlite+aiosqlite:///./room_reservations.db
SECRET = Секретное слово
FIRST_SUPERUSER_EMAIL = E-mail суперпользователя, который создастся при запуске приложения
FIRST_SUPERUSER_PASSWORD = Пароль суперпользователя, который создастся при запуске приложениял

Поля из конфигурационного файла Google API

EMAIL = '...'
TYPE = '...'
PROJECT_ID = '...'
PRIVATE_KEY_ID = "..."
PRIVATE_KEY =  "-----BEGIN PRIVATE KEY-----....-----END PRIVATE KEY-----\n"
CLIENT_EMAIL =  "rdmcloud@python-dev-402207.iam.gserviceaccount.com" # Почта сервисного аккаунта
CLIENT_ID =  "..."
AUTH_URI = "..."
TOKEN_URI =  "..."
AUTH_PROVIDER_X509_CERT_URL =  "..."
CLIENT_X509_CERT_URL = "..."
UNIVERSE_DOMAIN = "..."
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

На данный момент добавление и изменение переговорок, бронирований и пользователей работает через документацию Swagger
- http://127.0.0.1:8000/docs

В планах добавить более удобный для пользователя интерфейс.
