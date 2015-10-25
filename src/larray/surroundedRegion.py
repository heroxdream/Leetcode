__author__ = 'hanxuan'


"""
Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
"""

def solve(board):
    """
    :param board:
    :return:
    """

    if not any(board):
        return

    h_len = len(board[0])
    v_len = len(board)

    for i in range(h_len):
        bfs(board, 0, i)
        bfs(board, v_len - 1, i)

    for i in range(v_len):
        bfs(board, i, 0)
        bfs(board, i, h_len - 1)

    for i in range(v_len):
        for j in range(h_len):
            if board[i][j] == 'O':
                board[i][j] = 'X'

    for i in range(v_len):
        for j in range(h_len):
            if board[i][j] == '+':
                board[i][j] = 'O'


def bfs(board, i, j):
    """
    :param board:
    :param i:
    :param j:
    :return:
    """

    h_len = len(board[0])
    v_len = len(board)

    if i < 0 or i >= v_len or j < 0 or j >= h_len:
        return

    if board[i][j] != 'O':
        return

    board[i][j] = '+'
    bfs(board, i - 1, j)
    bfs(board, i + 1, j)
    bfs(board, i, j - 1)
    bfs(board, i, j + 1)

if __name__ == '__main__':
    b0 = [
        ['O', 'X', 'X'],
        ['X', 'O', 'X'],
        ['X', 'X', 'X']
    ]
    solve(b0)
    print(b0)

    b1 = [
        ['X', 'O'],
        ['X', 'O']
    ]
    solve(b1)
    print(b1)

    b2 = [
        ['O']
    ]
    solve(b2)
    print(b2)
