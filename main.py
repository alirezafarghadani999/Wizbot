import asyncio
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


from handlers.StartHandler import StartHandler
from handlers.MessageHandler import MessageHandler

TOKEN = "7061932990:AAEsXWz3_sFmfJheER39JJGrSCXQUjR-gR8"
# proxy = 'socks5://127.0.0.1:2080'


dp = Dispatcher()


StartHandler(dp)
MessageHandler(dp)


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())