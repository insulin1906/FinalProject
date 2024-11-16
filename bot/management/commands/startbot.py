import asyncio
from django.core.management.base import BaseCommand
from bot.config import main


class Command(BaseCommand):
    help = "Запуск бота"

    def handle(self, *args, **kwargs):
        asyncio.run(main())


if __name__ == '__main__':
    asyncio.run(main())
