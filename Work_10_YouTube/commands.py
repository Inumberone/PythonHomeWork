from bot_config import dp, bot
from aiogram import types
from pytube import YouTube

file_name = ''
quality = 0

async def start_url(message: types.Message):
    global file_name
    await bot.send_message(message.from_user.id, f'{message.from_user.first_name}'
                                                 f', запустился бот для скачивания видео с YouTub ')
    await bot.send_message(message.from_user.id, f'{message.from_user.first_name}'
                                                 f', введи URL видео: ')
    file_name = message.text
    for char in file_name:
        if char.isdigit():
            await enter_int(message)


async def enter_int(message):
    await bot.send_message(message.from_user.id, f'{message.from_user.first_name}'
                                                 f', введи качество видео '
                                                 '(1 - 360p, 2 - 720p, 3 - 1080p): ')

async def format_resolution(message):
    global quality
    if message.text.isdigit():

        if int(message.text) == 1:
            quality = 360
        if int(message.text) == 2:
            quality = 720
        if int(message.text) == 3:
            quality = 1080
        else:
            await bot.send_message(message.from_user.id, f'{message.from_user.first_name} введи число: 1, 2, 3')
    else:
        await bot.send_message(message.from_user.id, f'{message.from_user.first_name}'
                                                     f', введи только число: 1, 2, 3')
    await you_tube_add(message)


async def you_tube_add(message):
    global quality
    global file_name
    yt_video = YouTube(file_name)
    await bot.send_message(message.from_user.id, f'{message.from_user.first_name}'
                                                 f'{quality}')
    yt_video.streams.filter(resolution=quality, file_extension='mp4').first().download(r"C:\Users\Иван\Desktop")










