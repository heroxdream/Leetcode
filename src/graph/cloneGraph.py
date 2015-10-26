__author__ = 'hanxuan'


"""
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
"""

from graph.UndirectedGraphNode import UndirectedGraphNode

class Solution(object):
    def cloneGraph(node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node:
            return node

        seen = {}
        return dfs(node, seen)


def dfs(node, seen):
    """
    """

    label = node.label
    new_node = UndirectedGraphNode(label)
    seen[node.label] = new_node

    neighbors = []
    for n in node.neighbors:
        if n.label not in seen:
            neighbors.append(dfs(n, seen))
        else:
            neighbors.append(seen[n.label])

    new_node.neighbors = neighbors
    return new_node
