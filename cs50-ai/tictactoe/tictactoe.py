"""
Tic Tac Toe Player
"""

import math
import copy
import random

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_x = 0
    count_o = 0
    for row in board:
        for col in row:
            if col == X:
                count_x += 1
            elif col == O:
                count_o += 1
    if count_x > count_o:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if not col:
                actions.add((i, j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if not action:
        raise IndexError("Action is None")
    i = action[0]
    j = action[1]
    if board[i][j]:
        raise IndexError("Invalid action")
    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for row in board:  # Check rows
        if row[0] == row[1] == row[2]:
            return row[0]

    for i in range(3):  # Check columns
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2]:  # Check diagonals
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0]:  # Check diagonals
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    for row in board:
        if EMPTY in row:
            return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        print("> Terminal", board)
        return None

    print("Calculating...")

    best_action = actions(board).pop()
    print("> First action:", best_action)

    # Maximize X
    if player(board) == X:
        if board == initial_state():  # If empty board, return random action
            return random.choice(list(actions(board)))
        v = -math.inf
        temp = v
        for action in actions(board):
            print("> Action:", action)
            temp = max(v, min_value(result(board, action)))
            if temp > v:
                v = temp
                best_action = action
            if v == 1:  # If X can win, return that action
                return action

    # Minimize O
    else:
        v = math.inf
        temp = v
        for action in actions(board):
            temp = min(v, max_value(result(board, action)))
            if temp < v:
                v = temp
                best_action = action
            if v == -1:  # If O can win, return that action
                return action

    print("> Best action:", best_action)
    return best_action


def min_value(board):
    v = math.inf
    temp = v

    if terminal(board):  # base case
        return utility(board)
    for action in actions(board):
        temp = min(v, max_value(result(board, action)))  # find the minimum value
        if temp < v:
            v = temp
    return v


def max_value(board):
    v = -math.inf
    temp = v

    if terminal(board):  # base case
        return utility(board)
    for action in actions(board):
        temp = max(v, min_value(result(board, action)))  # find the maximum value
        if temp > v:
            v = temp
    return v
