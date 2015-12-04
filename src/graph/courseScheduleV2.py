"""
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed
as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to
finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses,
return an empty array.

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order
 is [0,1]

4, [[1,0],[2,0],[3,1],[3,2]]
There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1
and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering
is[0,2,1,3].
"""

counter = 0


def canFinish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: List[int]
    """

    graph = [[] for _ in range(numCourses)]
    visited = [0 for _ in range(numCourses)]
    location = [-1 for _ in range(numCourses)]

    global counter
    counter = numCourses - 1

    # initialized graph
    for x, y in prerequisites:
        graph[x].append(y)

    for n in range(numCourses):
        if dfs_cycle_detected(graph, n, visited, location):
            return []

    d = {}
    for i in range(len(location)):
        d[location[i]] = i

    location.sort(reverse=True)

    order = [d[i] for i in location]

    return order


def dfs_cycle_detected(graph, node, visited, location):

    global counter

    if visited[node] == -1:
        return True     # find node on path

    if visited[node] == 1:
        return False    # safe node

    visited[node] = -1     # set node on path

    for j in graph[node]:
        if dfs_cycle_detected(graph, j, visited, location):
            return True

    visited[node] = 1   # set node safe
    location[node] = counter
    counter -= 1

    return False

if __name__ == '__main__':

    n0 = 2
    p0 = [
        [0, 1]
    ]

    n1 = 4
    p1 = [
        [1, 0],
        [2, 0],
        [3, 1],
        [3, 2]
    ]

    n2 = 1
    p2 = []

    print(canFinish(n0, p0))

    print(canFinish(n1, p1))

    print(canFinish(n2, p2))
