import asyncio
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


from handlers.StartHandler import StartHandler
from handlers.MessageHandler import MessageHandler

class app:
    def __init__(self,TOKEN) -> None:
        self.dp = Dispatcher()
        self.TOKEN = TOKEN

        StartHandler(self.dp)
        MessageHandler(self.dp)




    def start(self):
        async def main() -> None:
            bot = Bot(token=self.TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
            await self.dp.start_polling(bot)
        
        asyncio.run(main())
        