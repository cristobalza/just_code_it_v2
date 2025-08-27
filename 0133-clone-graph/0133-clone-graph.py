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
        old_to_new_hmap = {}

        def dfs(node):
            if not node:
                return None
                
            if node in old_to_new_hmap:
                return old_to_new_hmap[node]

            copy_node = Node(node.val)
            old_to_new_hmap[node] = copy_node

            for neigh in node.neighbors:
                copy_node.neighbors.append(dfs(neigh))

            return copy_node

        return dfs(node)
        
