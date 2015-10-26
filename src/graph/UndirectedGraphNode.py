__author__ = 'hanxuan'


"""
Definition for a undirected graph node
"""

class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []