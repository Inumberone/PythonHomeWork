from random import randint as rnd

total_candy = 150
take_candy = 0
player_candy = 0
bot_candy = 0


def start_game():
    print('На столе лежит 150 конфет, задача игроков брать эти конфеты по очереди, но не более 28 штук за один раз.\n Тот кто заберет все конфеты последним за последний ход, тот победит')
    walk_first()

def walk_first():
    number_walk = rnd(1, 2)
    if number_walk == 1:
        player_turn()
    else:
        bot_turn()


def player_turn():
    global total_candy
    global take_candy
    global player_candy
    print(f'Твой ход, на столе {total_candy} конфет')
    take_candy = int(input('Сколько конфет ты возьмешь?: '))
    while take_candy > 28 or take_candy < 0 or take_candy > total_candy:
        take_candy = int(input('Ах ты жадина! Возьми конфет меньше!: '))
    total_candy -= take_candy
    player_candy += take_candy
    print(f'На столе осталось {total_candy} конфет')
    if total_candy > 0:
        bot_turn()
    else:
        print('Поздравляю! Ты победил сладкоежка')


def bot_turn():
    global total_candy
    global take_candy
    global bot_candy
    take_candy = total_candy % 29 if total_candy % 29 != 0 else rnd(1, 28)
    total_candy -= take_candy
    bot_candy += take_candy
    print(f'бот взял {take_candy} конфет')
    if total_candy > 0:
        player_turn()
    else:
        print('Тупой бот победил, ешь больше сладкого, заряжай мозги')

