__author__ = 'hanxuan'

"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

def generate(numRows):
    """
    :param numRows: int
    :return: List[List[int]]
    """

    if numRows <= 0:
        return []

    result = [
        [1]
    ]
    for _ in range(numRows - 1):
        parents = result[-1]
        children = [1]
        for i in range(len(parents) - 1):
            children.append(parents[i] + parents[i + 1])
        children.append(1)
        result.append(children)
    return result


"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
"""
def getRow(rowIndex):
    """
    :param rowIndex: int [1, ∞]
    :return: List[int]
    """

    if rowIndex <= 0:
        return []

    current_row = [1]
    for _ in range(rowIndex - 1):
        children = [1, 1]
        for i in range(len(current_row) - 1):
            children.index(1, current_row[i] + current_row[i + 1])
        current_row = children
    return current_row


if __name__ == '__main__':
    print(generate(2))
