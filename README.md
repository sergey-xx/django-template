# django-template

Шаблон проекта включающий:
- django
- django-restframework
- celery-worker
- celery-beat
- redis
- nginx

Запуск проекта в контейнере (предварительно переименовать .env.example в .env):
```
docker compose up
```
При первом запуске beat ожидаемо упадет, т.к. надо выполнить миграции:
```
docker compose exec backend python manage.py migrate
```
Создать супер-пользователя:
```
docker compose exec backend python manage.py createsuperuser --username admin --email admin@admin.ru
```
Собрать статику для api и админки:
```
docker compose exec backend python manage.py collectstatic
```
Запустить разовую тестовую фоновую задачу:
```
docker compose exec backend python manage.py taskrun
```
Запустить регулярную тестовую фоновую задачу (в кавычках CRON-расписание):
```
docker compose exec backend python manage.py schedulerun "* * * * *"
```
