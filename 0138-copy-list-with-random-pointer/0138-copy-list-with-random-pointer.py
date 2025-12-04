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
        """
        Deep copy steps: - the references have been severed

        1. Destroy current references and store them in some data structure 

        2. From that data structure, build it up from the original

        """

        if not head:
            return 

        # Step 1
        curr = head
        hmap = {} # original: copy 

        while curr:
            copied_node = Node(curr.val)
            hmap[curr] = copied_node # original: copy
            curr = curr.next 

        # Step 2
        curr = head

        while curr:

            copied_node = hmap[curr]

            if curr.next:
                copied_node.next = hmap[curr.next]

            if curr.random:
                copied_node.random = hmap[curr.random]

            curr = curr.next

        return hmap[head]



        