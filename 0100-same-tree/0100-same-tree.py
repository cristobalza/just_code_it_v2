# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(node, q):

            if not node and not q:
                return True

            if not node or not q:
                return False

            if node.val != q.val:
                return False

            l = dfs(node.left, q.left)
            r = dfs(node.right, q.right)

            return l and r

        return dfs(p, q)