from aiogram import Dispatcher, html
from aiogram.filters import CommandStart
from aiogram.types import Message , InlineKeyboardButton, InlineKeyboardMarkup ,callback_query
from aiogram.methods import set_chat_menu_button


from models.StartModel import StartModel

class StartHandler:
    def __init__(self,dispatcher):
        @dispatcher.message(CommandStart())
        async def command_start_handler(message: Message) -> None:
            model = StartModel(message,dispatcher)
            await message.answer(text=model.text(),reply_markup=model.inline_button())

        @dispatcher.callback_query(lambda c: c.data == 'login')
        async def login_button_handler(callback_query: callback_query) -> None:
            await callback_query.message.delete()

        