"""
Tic Tac Toe Player
"""

from cmath import inf
from copy import deepcopy
from operator import itemgetter

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_num = 0
    o_num = 0
    
    # Calculate the X and O numbers to define the next player
    for i in [0, 1, 2]:
        for j in [0, 1, 2]:
            if board[i][j] == X:
                x_num += 1
            
            elif board[i][j] == O:
                o_num += 1

    # Compare X_num and O_Num to calculute whose turn 
    if x_num == o_num:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Initialize A ction set
    action = set()
    
    for i in [0, 1, 2]:
        for j in [0, 1, 2]:
            if board[i][j] == EMPTY:
                action.add((i , j))
    return action
    
def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    (x, y) = action

    if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
        raise IndexError

    actionarray = [row[:] for row in board]
    actionarray[x][y] = player(board)

    return actionarray



def check_rows(board):
    # Check rows      
    for i in [0, 1, 2]:
        j = 0
        if board[i][j] == board[i][j+1] == board[i][j+2]:
            return board[i][j]

def check_cols(board):
    # Check Columns 
    for j in [0, 1, 2]:
        i = 0
        if board[i][j] == board[i+1][j] == board[i+2][j]:
            return board[i][j]

def check_diagonals(board):
    # Check Diagonals
    i = 0
    j = 0

    if board[i][j] == board[i+1][j+1] == board[i+2][j+2]:
        return board[i][j]
    

    if board[i][j+2] == board[i+1][j+1] == board[i+2][j]:
        return board[i][j+2]

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if check_rows(board):
        return check_rows(board)

    if check_cols(board):
        return check_cols(board)

    if check_diagonals(board):
        return check_diagonals(board)

    # if no winner, so return None
    return None

def check_empty(board):
    # Check for empty cells if no empty cells it is a terminal board
    for i in [0, 1, 2]:
        for j in [0, 1, 2]:
            # Check if the game still in progress, return false if there is empty cells
            if board[i][j] == EMPTY:
                    return False
    return True

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # check if there is a winner
    if winner(board) or check_empty(board):
        return True
    
    # IF empty cells, and No winner
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0

def MAX(state):
    if terminal(state):
        return utility(state)
    
    v = -1

    for action in actions(state):
        v = max(v, MIN(result(state, action)))
    return v

def MIN(state):
    if terminal(state):
        return utility(state)
    
    v = 1

    for action in actions(state):
        v = min(v, MAX(result(state, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    #check if it terminal state
    if terminal(board):
        return None

    #get currrent player
    if player(board) == X:
        # get all available actions for current player and explore them
        # output list to store each action and its terminal_state utility [[utility, action]]
        output = []
        for action in actions(board):
            output.append([MIN(result(board, action)), action])

        # Get the optimal_action, The action with the higest utility
        optimal_action = sorted(output, key=itemgetter(0), reverse= True)[0][1]
      
        return optimal_action
        
    #get currrent player
    if player(board) == O:
        # get all available actions for current player and explore them
        # output list to store each action and its terminal_state utility [[utility, action]]
        output = []
        for action in actions(board):
            output.append([MAX(result(board, action)), action])

        #Get the optimal_action, The action with the lowest utility
        optimal_action = sorted(output, key=itemgetter(0))[0][1]
      
        return optimal_action   