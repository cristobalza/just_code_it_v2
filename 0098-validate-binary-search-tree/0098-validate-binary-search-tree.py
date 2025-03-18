# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, all_min, all_high):

            if not node:
                return True

            if all_high <= node.val or node.val <= all_min:
                return False


            left = dfs(node=node.left, all_min=all_min, all_high=node.val)
            right = dfs(node=node.right, all_min=node.val, all_high=all_high)

            return left and right


        return dfs(node=root, all_min=float("-inf"), all_high=float("inf"))

        