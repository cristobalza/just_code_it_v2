"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        def dfs(node):

            if node in hmap:
                return hmap[node]

            if not node:
                return 
            
            hmap[node] = Node(node.val)

            for neigh in node.neighbors:
                hmap[node].neighbors.append(dfs(neigh))
            
            return hmap[node]

        hmap = {} # old node: copy node

        return dfs(node)