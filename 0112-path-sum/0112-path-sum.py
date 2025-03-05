# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, total):
            if not node:
                return False
            if node.val + total == targetSum and not node.left and not node.right:
                return True

            left = dfs(node.left, node.val + total)
            right = dfs(node.right, node.val + total)

            return left or right

        return dfs(root, 0)