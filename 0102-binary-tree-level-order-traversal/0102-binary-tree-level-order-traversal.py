# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        q = collections.deque()

        q.append(root)

        res = []

        while q:

            nodes = len(q)
            level_subset = []
            for _ in range(nodes):
                node = q.popleft()
                level_subset.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if level_subset:
                res.append(level_subset)

        return res
        