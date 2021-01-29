
def draw_field(field):
    print('\n     C  1  2  3')
    print('   R')
    print('   1    '+'  '.join(field[0]))
    print('   2    '+'  '.join(field[1]))
    print('   3    '+'  '.join(field[2]))
    print()

def make_turn(field, turn, symbol):
    if field[turn[0]][turn[1]] == ' ':
        field[turn[0]][turn[1]] = symbol
        return True
    return False

def evaluate_game(field):
    field_set = [{None} for i in range(len(field))]
    field_rotated_set = [{None} for i in range(len(field[0]))]
    field_diagonals_set = [{None}, {None}]

    for row in range(len(field)):
        for column in range(len(field[row])):
            element = field[row][column]
            field_set[row].add(element)
            field_rotated_set[column].add(element)
            if row == column:
                field_diagonals_set[0].add(element)
            if row == (len(field[row]) - column - 1):
                field_diagonals_set[1].add(element)

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

    return ' '

def test_turn(field, turn):

    return False

if __name__ == '__main__':

#    print('Консольная игра в кресики нолики. \n\n')

#    player1_name = input('Ввдедите имя первого игрока (играет крестиками):')
#    player2_name = input('Ввдедите имя второго игрока (играет ноликами):')

    play_field = [['X', 'O', 'O'], ['O', 'O', 'X'], ['X', 'O', 'X']]
    draw_field(play_field)
    turn = [1, 1]
    print(evaluate_game(play_field))

#    moove = True
#    player = 1
#    while moove:
#        if player == 1:
#            draw_field(play_field)
#            turn = input(f'Ваш ход, {player1_name}:')
#            test_turn(play_field, turn)
#            make_turn(play_field, turn, player)

