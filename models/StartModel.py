from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import html

class StartModel:
    def __init__(self,message,dispatcher):
        self.message = message
        self.dispatcher = dispatcher

    def inline_button(self):
        profile_1 = InlineKeyboardButton(callback_data='login', text='ورود به ویزبات')
        btmap = InlineKeyboardMarkup(inline_keyboard=[[profile_1]])
        return btmap

    def text(self):
        text = f"""
سلام خوش اومدی {html.bold(self.message.chat.full_name)}
من ویزباتم میتونم کانالتو با خیال خوش به من بسپاری
کار هایی که ویزبات میتونه انجام بده 

+ ادمین کردن در یک بازه زمانی با یوزر پسورد
+ مدریت تبلیغات شما
+ محدود کردن دسترسی ادمین ها در یک بازه زمانی خاص
+ تولید پست با استفاده از هوش مصنوعی
        """
        return text
