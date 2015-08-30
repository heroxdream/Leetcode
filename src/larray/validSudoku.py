__author__ = 'hanxuan'

def validSudoku(board):
    """
    :param board: List[List[string]]
    :return: book
    Determine if a Sudoku is valid
    """

    n = 9
    row_sets = []
    col_sets = []
    for i in range(n):
        row_sets.append(set())
        col_sets.append(set())

    m = 3
    row_col_sets = [[set() for _ in range(m)] for _ in range(m)]    # be careful

    for i in range(n):
        for j in range(n):
            e = board[i][j]
            if e != '.':
                num = int(e)
                if num in row_sets[i] or num in col_sets[j] or num in row_col_sets[i//m][j//m]:
                    return False
                row_sets[i].add(num)
                col_sets[j].add(num)
                row_col_sets[i//m][j//m].add(num)

    return True


if __name__ == '__main__':
    board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    board2 =[
        ".87654321",
        "2........",
        "3........",
        "4........",
        "5........",
        "6........",
        "7........",
        "8........",
        "9........"]

    print(validSudoku(board2))
