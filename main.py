
def draw_field(field):
    print('\n     C  1  2  3')
    print('   R')
    print('   1    '+'  '.join(field[0]))
    print('   2    '+'  '.join(field[1]))
    print('   3    '+'  '.join(field[2]))
    print()

def make_turn(field, turn, player):
    if field[turn[0]][turn[1]] == ' ':
        field[turn[0]][turn[1]] = player
        return True
    return False

def evaluate_game(field):

    return

def test_turn(field, turn):

    return False

if __name__ == '__main__':

#    print('Консольная игра в кресики нолики. \n\n')

#    player1_name = input('Ввдедите имя первого игрока (играет крестиками):')
#    player2_name = input('Ввдедите имя второго игрока (играет ноликами):')

    play_field = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    draw_field(play_field)
    turn = [1, 1]
    print(make_turn(play_field, turn, 'X'))
    draw_field(play_field)
    turn = [1, 0]
    print(make_turn(play_field, turn, 'O'))
    draw_field(play_field)

#    moove = True
#    player = 1
#    while moove:
#        if player == 1:
#            draw_field(play_field)
#            turn = input(f'Ваш ход, {player1_name}:')
#            test_turn(play_field, turn)
#            make_turn(play_field, turn, player)

