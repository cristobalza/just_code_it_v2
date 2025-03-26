# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, curr_sum):

            if not node:
                return False

            if curr_sum - node.val == 0 and not node.left and not node.right:
                return True

            left = dfs(node.left, curr_sum - node.val)
            right = dfs(node.right, curr_sum - node.val)

            return left or right

        return dfs(root, targetSum)

        