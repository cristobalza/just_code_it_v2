"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        hmap = {}

        curr = head
        while curr:
            copy_node = Node(curr.val)
            hmap[curr] = copy_node

            curr = curr.next

        curr = head
        while curr:
            node = hmap[curr]
            node.next = hmap[curr.next] if curr.next else None
            node.random = hmap[curr.random] if curr.random else None
            
            curr = curr.next

        return hmap[head]