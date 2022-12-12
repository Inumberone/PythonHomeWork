def print_field(field: list):
    print(f' {field[0]} | {field[1]} | {field[2]} ')
    print('-----------')
    print(f' {field[3]} | {field[4]} | {field[5]} ')
    print('-----------')
    print(f' {field[6]} | {field[7]} | {field[8]} ')


def enter_player_turn(field: list, mark: str):
    while True:
        try:
            turn = int(input(f'Ход {mark}. Введите номер ячейки: '))

            if 0 < turn < 10 and field[turn-1].isdigit():
                return turn
            else:
                print('Эта ячейка занята или не существует')
        except:
            print('Введите целое число')