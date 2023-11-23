# vote_team73

## links(для контейнерной сборки. для локальной по умолчанию порт 8000)
http://127.0.0.1:80/

http://127.0.0.1:80/swagger/

http://127.0.0.1:80/admin/

# Доступ в админку
### login: admin
### password: admin
#

# Deploy в Docker
### ``docker-compose up -d --build``
### При деплое c Докера накатывается дамп с начальными данными, логин пароль от админки: admin admin
#


# Развернуть локально
### Чтобы развернуть локально нужно закомментировать 40-43 строки в project/settings.py
### Нужно в .env в корне проекта раскомментировать необходимые конфиги(они подписаны)
### ``pip install poetry``
### ``poetry install``
### ``poetry shell``
### `python manage.py migrate`
### `python manage.py loaddata dump.json`
### `python manage.py runserver`

### Подергать ручки можно в tests/main.http (В любой Jetbrains IDE)


