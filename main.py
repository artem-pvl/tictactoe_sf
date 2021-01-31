
def draw_field(field):
    print('\n     C  1  2  3')
    print('   R')
    print('   1    '+'  '.join(field[0]))
    print('   2    '+'  '.join(field[1]))
    print('   3    '+'  '.join(field[2]))
    print()


def make_turn(field, this_turn, symbol):
    if not ((0 < this_turn[0] < 4) and (0 < this_turn[1] < 4)):
        return False
    if field[this_turn[0]-1][this_turn[1]-1] == ' ':
        field[this_turn[0]-1][this_turn[1]-1] = symbol
        return True
    return False


def evaluate_game(field):
    field_set = [{None} for i in range(len(field))]
    field_rotated_set = [{None} for i in range(len(field[0]))]
    field_diagonals_set = [{None}, {None}]
    free_cells = False

    for row in range(len(field)):
        for column in range(len(field[row])):
            element = field[row][column]
            field_set[row].add(element)
            field_rotated_set[column].add(element)
            if row == column:
                field_diagonals_set[0].add(element)
            if row == (len(field[row]) - column - 1):
                field_diagonals_set[1].add(element)
            if not free_cells:
                free_cells = (element == ' ')

    for row in field_set:
        row = row.difference({None})
        if len(row) == 1 and ' ' not in row:
            return row.pop()

    for row in field_rotated_set:
        row = row.difference({None})
        if len(row) == 1 and ' ' not in row:
            return row.pop()

    for row in field_diagonals_set:
        row = row.difference({None})
        if len(row) == 1 and ' ' not in row:
            return row.pop()

    if not free_cells:
        return '-'

    return ' '


def turn(a, b):
    while True:
        yield a
        yield b


def check_turn(player_name, turn_str):
    turns_range = [str(ch) for ch in range(1, 4)]
    checked_turn = ''
    checked_turn = checked_turn.join([i for i in list(turn_str) if i in turns_range])
    while not (len(checked_turn) == 2):
        checked_turn = ''
        turn_tmp = input(f'Попробуйте ввести ход ещё раз - 2 цйфры: строка столбец (RC), {player_name}: ')
        checked_turn = checked_turn.join([i for i in list(turn_tmp) if i in turns_range])
    return checked_turn


if __name__ == '__main__':

    print('\nКонсольная игра в кресики нолики. \n\n')
    player1_name = input('Ввдедите имя первого игрока (играет крестиками): ')
    player2_name = input('Ввдедите имя второго игрока (играет ноликами): ')
    print('\nХоды вводится цифрами в формате: <строка> <столбец>\n')

    play_field = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    current_player_iter = turn('X', 'O')

    game_result = ' '
    while game_result == ' ':
        current_player = next(current_player_iter)
        current_player_name = player1_name if current_player == "X" else player2_name
        draw_field(play_field)

        game_turn = input(f'Ваш ход, {current_player_name} ({current_player}): ')
        game_turn = check_turn(current_player_name, game_turn)

        while not make_turn(play_field, list(map(int, list(game_turn))), current_player):
            game_turn = input(f'Ход не корректен! Попробуйте ещё раз, {current_player_name}: ')
            while not (game_turn.isdigit() and len(game_turn) == 2):
                game_turn = input(f'Попробуйте ввести ход ещё раз, {current_player_name}:')

        game_result = evaluate_game(play_field)

    draw_field(play_field)
    if game_result == 'X':
        print(f'Победил {player1_name}! (X)')
    elif game_result == 'O':
        print(f'Победил {player2_name}! (O)')
    else:
        print('Ничья!')
