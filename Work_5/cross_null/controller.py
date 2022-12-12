import random

import bot
import view
import model

def start_game():
    first_turn = random.randint(0,1)
    if first_turn == 1:
        model.set_first_turn(True)
    else:
        model.set_first_turn(False)
    while True:
        game()


def player_turn():
    field = model.get_field()
    mark = model.get_mark()
    turn = view.enter_player_turn(field, mark)
    model.set_field(turn)
    if model.check_win():
        print(f'Победил {model.get_mark()}')
        exit()
    if model.check_tie():
        print(f'Ничья, тупые уроды')
        exit()
    model.switch_mark()

def enemy_turn():
    field = model.get_field()
    mark = model.get_mark()
    turn = bot.ai_logic(field)
    model.set_field(turn)
    print(f'Соперник {mark} сделал ход в клетку {turn}\n')
    if model.check_win():
        print(f'Победил {model.get_mark()}')
        exit()
    if model.check_tie():
        print(f'Ничья, тупые уроды')
        exit()
    model.switch_mark()

def game():
    game = model.get_first_turn()
    field = model.get_field()
    if game:
        view.print_field(field)
        player_turn()
        enemy_turn()
    else:
        enemy_turn()
        view.print_field(field)
        player_turn()