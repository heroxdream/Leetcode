__author__ = 'hanxuan'


"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water
and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the
grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
"""

def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                ans += 1
                DFSMark(grid, i, j)
    return ans

def DFSMark(grid, i, j):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
        return
    grid[i][j] = '0'
    DFSMark(grid, i, j + 1)
    DFSMark(grid, i, j - 1)
    DFSMark(grid, i + 1, j)
    DFSMark(grid, i - 1, j)

