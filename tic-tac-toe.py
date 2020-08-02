def play_tic_tac_toe():
    
    # Using booleans and while loops throughout for control flow throughout the game play.
    playing = True
    
    # The board is represented as one list object with each row a nested list.
    board = [['','',''],['','',''],['','','']]

    player = 'X'

    print_board(board)

    while playing:
        # Print who's turn it is.
        print(f'Player {player} turn.')
        # Select row and position to play.
        player, board = take_turn(player, board)
        # Show new board
        print_board(board)
        
        # Check if the player won with their play.
        winner = check_winner(board)
        if winner != '':
            print(f'{winner} wins!')
            print('')
            # If the player wins, the game is over
            playing = False

        # If the play didn't win, check if there's a tie.
        tie = check_tie(board)
        if tie:
            print('Tie Game!')
            print('')
            # if there's a tie the game is over.
            playing = False

    # After there is a winner or tie ask if the players would like to play again.
    asking_to_play_again = True
    play_again = input('Want to play again? Y or N: ')
    while  asking_to_play_again:
        # check input is within range. If not ask for input again.
        if play_again.lower() not in ['y','n']:
            print("I didn't understand that. Please enter Y for yes or N for no.")
        elif play_again.lower() == 'y':
            # if they want to play again, start another game
            play_tic_tac_toe()
        else:
            # if they don't want to play again, end program.
            asking_to_play_again = False


def print_board(board):
    # used to print out the board throughout the game process.
    print('')
    print('Row 1: ', board[0])
    print('Row 2: ', board[1])
    print('Row 3: ', board[2])
    print('')


def take_turn(player, board):
    
    taking_turn = True
    while taking_turn:
        
        # initiating variables at top of loop so they're accessible throughout.
        play_row = int
        play_position = int
        
        selecting_row = True
        while selecting_row:  
            play_row = input('Enter row number to play: ')
            # Expecting 1, 3 or 3 for row and position expecting player not to assume 0 indexing. Will adjust by subtracting 1 below.
            if play_row not in ['1', '2', '3']:
                print("I didn't understand that. Enter 1, 2, or 3")
            else:
                play_row = int(play_row) - 1
                selecting_row = False

        selecting_position = True
        while selecting_position:  
            play_position = input('Enter position to play: ')
            # Expecting 1, 3 or 3 for row and position expecting player not to assume 0 indexing. Will adjust by subtracting 1 below.
            if play_position not in ['1', '2', '3']:
                print("I didn't understand that. Enter 1, 2, or 3")
            else:
                play_position = int(play_position) - 1
                selecting_position = False

        # Check if the player's choice is an open position on the board and place their mark if so, otherwise ask them to make another choice.
        if board[play_row][play_position] == '': 
            board[play_row][play_position] = player
            taking_turn = False
        else:
            print('')
            print('That position is taken. Please choose another position.')
            print('')

    # Setting the player for the next turn.
    if player == 'X':
        player = 'O'
    else:
        player = 'X'

    return player, board

def check_winner(board):
    winner = ''

    # Check winning combinations for each player and return winning player if winning condition met.

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

    # Check if all positions taken. If so, the game is a tie.

    if board[0][0] != '' and board[0][1] != '' and board[0][2] != '' \
    and board[1][0] != '' and board[1][1] != '' and board[1][2] != '' \
    and board[2][0] != '' and board[2][1] != '' and board[2][2] != '':
        tie = True
    return tie


if __name__ == "__main__":
    play_tic_tac_toe()