from django.core.management.base import BaseCommand

from project.celery import debug_task

URL = 'https://www.cbr-xml-daily.ru/daily_json.js'


class Command(BaseCommand):
    """Команда для моментального выполнения."""

    help = 'Sync rates data command.'

    def handle(self, *args, **options):
        debug_task.delay()
