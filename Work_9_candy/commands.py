from random import randint as rnd
from bot_config import dp, bot
from aiogram import types

total_candy = 150
take_candy = 0
player_candy = 0
bot_candy = 0


@dp.message_handler(commands=['return'])
@dp.message_handler(commands=['start'])
async def start_game(message: types.Message):
    global total_candy
    global take_candy
    global bot_candy
    global player_candy
    total_candy = 150
    player_candy = 0
    bot_candy = 0
    await bot.send_message(message.from_user.id, f'{message.from_user.first_name}'
                                                     f', на столе лежит {total_candy} конфет, задача игроков брать эти конфеты по '
                                                     f'очереди, но не более 28 штук за один раз. '
                                                     f' Тот кто заберет все конфеты последним за последний ход, тот победит. Для игры вновь, введи: /start')
    await walk_first(message)


async def walk_first(message):
    number_walk = rnd(1, 2)
    if number_walk == 1:
        await player_turn(message)
    else:
        await bot_turn(message)


async def bot_turn(message):
    global total_candy
    global take_candy
    global bot_candy
    if total_candy > 28:
        take_candy = total_candy % 29 if total_candy % 29 != 0 else rnd(1, 28)
    else:
        take_candy = total_candy
    total_candy -= take_candy
    bot_candy += take_candy
    await bot.send_message(message.from_user.id, f'бот взял {take_candy} конфет, на столе осталось {total_candy}')
    if total_candy > 0:
        await player_turn(message)
    else:
        await bot.send_message(message.from_user.id, f'{message.from_user.first_name}'
                                                     f' , не расстраивайся, против тебя играл умный бот, кстати он '
                                                     f'набрал {bot_candy} '
                                                     f'конфет, а ты {player_candy}')


async def player_turn(message):
    await bot.send_message(message.from_user.id, f'{message.from_user.first_name}'
                                                 f', твой ход')


@dp.message_handler()
async def start_bot(message: types.Message):
    global total_candy
    global player_candy

    if message.text.isdigit():
        if 0 < int(message.text) < 29:
            total_candy -= int(message.text)
            player_candy += int(message.text)
            await bot.send_message(message.from_user.id, f'{message.from_user.first_name}'
                                                         f' взял со стола {message.text} конфет. '
                                                         f'на столе осталось {total_candy}')
            if total_candy > 0:
                await bot_turn(message)

            else:
                await bot.send_message(message.from_user.id, f'{message.from_user.first_name}'
                                                             f', поздравляю! ты победил сладкоежка, ты набрал {player_candy} конфет')
                total_candy = 150
                take_candy = 0
                player_candy = 0
                bot_candy = 0
        else:
            await message.reply(f'{message.from_user.first_name} да ты жадина, не хочешь ли взять поменьше:')
    else:
        await bot.send_message(message.from_user.id, f'{message.from_user.first_name}'
                                                     f' напиши сколько хочешь взять конфет цифрами')

