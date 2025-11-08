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
            node = Node(curr.val)
            hmap[curr] = node
            curr = curr.next

        curr = head
        while curr:
            node = hmap[curr]
            if curr.next:
                node.next = hmap[curr.next]
            else:
                node.next = None

            if curr.random:
                node.random = hmap[curr.random]
            else:
                node.random = None

            curr = curr.next

        return hmap[head]

        