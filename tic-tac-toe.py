def play_tic_tac_toe():
    
    playing = True
    
    board = [['','',''],['','',''],['','','']]

    player = 'X'

    print_board(board)

    while playing:
        print(f'Player {player} turn.')
        player, board = take_turn(player, board)
        print_board(board)
        
        winner = check_winner(board)
        if winner != '':
            print(f'{winner} wins!')
            print('')
            playing = False

        tie = check_tie(board)
        if tie:
            print('Tie Game!')
            print('')
            playing = False

    asking_to_play_again = True
    play_again = input('Want to play again? Y or N: ')
    while  asking_to_play_again:
        if play_again.lower() not in ['y','n']:
            print("I didn't understand that. Please enter Y for yes or N for no.")
        elif play_again.lower() == 'y':
            play_tic_tac_toe()
        else:
            asking_to_play_again = False


def print_board(board):
    print('')
    print('Row 1: ', board[0])
    print('Row 2: ', board[1])
    print('Row 3: ', board[2])
    print('')


def take_turn(player, board):
    
    taking_turn = True
    while taking_turn:
        play_row = int
        play_position = int
        
        selecting_row = True
        while selecting_row:  
            play_row = input('Enter row number to play: ')
            if play_row not in ['1', '2', '3']:
                print("I didn't understand that. Enter 1, 2, or 3")
            else:
                play_row = int(play_row) - 1
                selecting_row = False

        selecting_position = True
        while selecting_position:  
            play_position = input('Enter position to play: ')
            if play_position not in ['1', '2', '3']:
                print("I didn't understand that. Enter 1, 2, or 3")
            else:
                play_position = int(play_position) - 1
                selecting_position = False

        if board[play_row][play_position] == '': 
            board[play_row][play_position] = player
            taking_turn = False
        else:
            print('')
            print('That position is taken. Please choose another position.')
            print('')

    if player == 'X':
        player = 'O'
    else:
        player = 'X'

    return player, board

def check_winner(board):
    winner = ''

    if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X':
        winner = 'X'
    elif board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X':
        winner = 'X'
    elif board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X':
        winner = 'X'
    elif board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X':
        winner = 'X'
    elif board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X':
        winner = 'X'
    elif board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X':
        winner = 'X'
    elif board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        winner = 'X'
    elif board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
        winner = 'X'
    elif board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O':
        winner = 'O'
    elif board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O':
        winner = 'O'
    elif board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O':
        winner = 'O'
    elif board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O':
        winner = 'O'
    elif board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O':
        winner = 'O'
    elif board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O':
        winner = 'O'
    elif board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
        winner = 'O'
    elif board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
        winner = 'O'
    else:
        pass

    return winner

def check_tie(board):
    tie = False
    if board[0][0] != '' and board[0][1] != '' and board[0][2] != '' \
    and board[1][0] != '' and board[1][1] != '' and board[1][2] != '' \
    and board[2][0] != '' and board[2][1] != '' and board[2][2] != '':
        tie = True
    return tie


play_tic_tac_toe()