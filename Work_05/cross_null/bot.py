import random

import model

def ai_logic(field: list) -> int:
    win = model.win
    mark = model.get_mark()
    if field[4].isdigit():
        return 5
    else:
        corner = [0,2,6,8]
        random.shuffle(corner)
        for opt in win:
            if (field[opt[0]] == field[opt[1]] == mark) and field[opt[2]].isdigit():
                return opt[2]+1
            if (field[opt[1]] == field[opt[2]] == mark) and field[opt[0]].isdigit():
                return opt[0]+1
            if (field[opt[0]] == field[opt[2]] == mark) and field[opt[1]].isdigit():
                return opt[1]+1
        for opt in win:
            if (field[opt[0]] == field[opt[1]] == model.get_enemy_mark()) and field[opt[2]].isdigit():
                return opt[2]+1
            if (field[opt[1]] == field[opt[2]] == model.get_enemy_mark()) and field[opt[0]].isdigit():
                return opt[0]+1
            if (field[opt[0]] == field[opt[2]] == model.get_enemy_mark()) and field[opt[1]].isdigit():
                return opt[1]+1
        for cell in corner:
            if field[cell].isdigit():
                return cell+1
        while True:
            turn = random.randint(1,9)
            if field[turn].isdigit():
                return turn+1