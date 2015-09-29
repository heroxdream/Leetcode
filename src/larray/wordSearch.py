__author__ = 'hanxuan'

"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally
or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""


def exist(board, word):
    """
    :param board:
    :param word:
    :return:
    """
    if not word:
        return True

    for i in range(len(board)):
        for j in range(len(board[i][0])):
            if lookup(board, word, i, j, set()):
                return True
    return False

def lookup(board, word, i, j, seen):
    """
    :param board:
    :param word:
    :param seen:
    :return:
    """
    if (i, j) in seen or i not in range(len(board)) or j not in range(len(board[i][0])):
        seen.add((i, j))
        return False

    seen.add((i, j))

    if len(word) == 1:
        return board[i][0][j] == word

    curr_char = word[0]
    rest_word = word[1:]

    return curr_char == board[i][0][j] and \
           (lookup(board, rest_word, i, j - 1, seen) or
            lookup(board, rest_word, i, j + 1, seen) or
            lookup(board, rest_word, i + 1, j, seen) or
            lookup(board, rest_word, i - 1, j, seen))


if __name__ == '__main__':
    board0 = [
        ["ABCE"],
        ["SFCS"],
        ["ADEE "]
    ]

    w0 = "ABCCED"
    w1 = "SEE"
    w2 = "ABCB"
    w3 = ' '

    board1 = [
        ['aa']
    ]

    # print(exist(board0, w0))
    # print(exist(board0, w1))
    # print(exist(board0, w2))
    # print(exist(board0, w3))

    print(exist(board1, 'aa'))
