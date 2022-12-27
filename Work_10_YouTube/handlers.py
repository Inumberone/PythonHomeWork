from aiogram import Dispatcher
import commands

def registred_handlers(dp: Dispatcher):
    dp.register_message_handler(commands.start_url, commands=['start'])
    dp.register_message_handler(commands.enter_int)