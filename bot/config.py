from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.enums.parse_mode import ParseMode
from bot.scrapper import search_products
from finalproject import settings


TOKEN = settings.TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    await message.reply("Привет! Отправь мне название товара.")


@dp.message()
async def search_handler(message: types.Message):
    query = message.text.strip()
    if not query:
        await message.reply("Пожалуйста, отправь название товара.")
        return

    await message.reply("Ищу товары, подождите...")

    products = await search_products(query)
    if "error" in products:
        await message.reply("Ошибка при поиске. Попробуйте позже.")
        return

    if not products:
        await message.reply("Ничего не найдено.")
    else:
        for product in products[:5]:
            await message.reply(
                f"**{product['title']}**\nЦена: {product['price']}\n[Ссылка на товар]({product['link']})",
                parse_mode=ParseMode.MARKDOWN
            )


async def main():
    await dp.start_polling(bot)


