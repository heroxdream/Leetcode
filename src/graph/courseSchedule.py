"""
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0
you should also have finished course 1. So it is impossible.
"""


def canFinish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """

    graph = [[] for _ in range(numCourses)]
    visited = [0 for _ in range(numCourses)]

    # initialized graph
    for x, y in prerequisites:
        graph[x].append(y)

    for n in range(numCourses):
        if dfs_cycle_detected(graph, n, visited):
            return False

    return True


def dfs_cycle_detected(graph, node, visited):

    print('node: ', node)

    if visited[node] == -1:
        return True     # find node on path

    if visited[node] == 1:
        return False    # safe node

    visited[node] = -1     # set node on path

    for j in graph[node]:
        if dfs_cycle_detected(graph, j, visited):
            return True

    visited[node] = 1   # set node safe

    return False

if __name__ == '__main__':

    n0 = 2
    p0 = [
        [0, 1],
        [1, 0]
    ]

    print(canFinish(n0, p0))
