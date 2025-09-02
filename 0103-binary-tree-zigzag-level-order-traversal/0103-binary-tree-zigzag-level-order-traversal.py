# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # bfs
        q = collections.deque()
        q.append(root)

        res = []

        zigzag = 0

        while q:

            children = len(q)
            subset = []
            for _ in range(children):

                node = q.popleft()

                subset.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            if zigzag % 2 == 0:
                res.append(subset)
            else:
                res.append(subset[::-1])

            zigzag += 1

        return res


        