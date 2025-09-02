"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        q = collections.deque()
        q.append(root)

        while q:

            children = len(q)

            prev = None

            for _ in range(children):

                node = q.popleft()

                if prev is not None:
                    prev.next = node

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

                # update prev
                prev = node
            
        return root



