# tic-tac-toe
Simple command-line version of tic-tac-toe written in Python.

## Control Flow
Throughout the program booleans and while loops are utilized for control flow.

## The Board
The tic-tac-board is one list object with nested lists to represent each row of the board.
This allows simple indexing to identify the row and position for each play.
Example: board[0][0] indicates the first position in the first row.

## Checking Win and Tie
After each play, the program check first for a win and then for a tie.
The order of these checks matter because the tie check only checks if all positions are filled regardless of whether the position is an 'X' or 'O'.
This makes it possible that a winning combination could also match the tie check.
To prevent a tie check from returning True when there is a winning condition win check are done first.

## Game Over
The game ends when either a winning condition or the tie condition are met.
After the end of the game, the program asks if the players would like to play again.
If so, a new game starts, if not the program ends.