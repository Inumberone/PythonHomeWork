field = ['1' ,'2' ,'3' ,'4' ,'5' ,'6' ,'7' ,'8' ,'9']
win = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
mark = 'X'
first_turn = ''

def get_mark():
    global mark
    return mark

def get_first_turn() -> bool:
    global first_turn
    return first_turn

def set_first_turn(turn: bool):
    global first_turn
    first_turn = turn
def get_enemy_mark():
    global mark
    global mark
    if mark == 'X':
        return 'O'
    else:
        return 'X'
def get_field():
    global field
    return field

def set_field(index: int):
    global field
    global mark
    field[index-1] = mark

def switch_mark():
    global mark
    if mark == 'X':
        mark = 'O'
    else:
        mark = 'X'

def check_win() -> bool:
    global field
    global win
    for opt in win:
        if (field[opt[0]] == field[opt[1]]  == field[opt[2]] ):
            return True
    return False

def check_tie() -> bool:
    global field
    for cell in field:
        if cell.isdigit():
            return False
    else:
        return True