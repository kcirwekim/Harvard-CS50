"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

# DONE
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
    count_X = 0
    count_O = 0
    
    # Cycle thru the board and count Xs and Ox
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == X:
                count_X += 1
            elif board[i][j] == O:
                count_O += 1

    # Determine player based on turn count
    if count_X > count_O:
        return O
    else:
        return X
    
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    cells = set()
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                cells.add((i, j))
    
    return cells

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # Set deepcopy
    copy_board = copy.deepcopy(board)
    
    #Check if it's an allowed move
    try:
        copy_board[action[0]][action[1]] = player(copy_board)
        return copy_board
    except:
        print(board, copy_board, action)
        
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winning_rows = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]]]
    
    if ['X', 'X', 'X'] in winning_rows:
        return X
    elif ['O', 'O', 'O'] in winning_rows:
        return O
    else:
           return None
    
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    CountEmpty = 0
    for i in board:
        for j in i:
            if j == EMPTY:
                CountEmpty += 1
    
    
    if winner(board) != None:
        return True
    elif CountEmpty == 0:
        return True
    else:
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
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value, move = X_Player(board)
            return move
        else:
            value, move = O_Player(board)
            return move


def X_Player(board):
    '''
    Returns an integer score and tuple (i, j) with the best move for X
    '''
    if terminal(board):
        return utility(board), None

    score = -math.inf
    move = None
    
    for action in actions(board):
        t, act = O_Player(result(board, action))
        if t > score:
            score = t
            move = action
            if score == 1:
                return score, move

    return score, move


def O_Player(board):
    '''
    Returns an integer score and tuple (i, j) with the best move for O
    '''
    
    if terminal(board):
        return utility(board), None

    score = math.inf
    move = None
    
    for action in actions(board):
        t, act = X_Player(result(board, action))
        if t < score:
            score = t
            move = action
            if score == -1:
                return score, move

    return score, move
    

