from aiogram import Dispatcher, html
from aiogram.types import Message

class MessageHandler:
    def __init__(self,dispatcher):        
        @dispatcher.message()
        async def echo_handler(message: Message) -> None:
            try:
                await message.send_copy(chat_id=message.chat.id)
            except TypeError:
                # But not all the types is supported to be copied so need to handle it
                await message.answer("Nice try!")

