# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, min_val, max_val):

            if not node:
                return True

            if node.val >= max_val or node.val <= min_val:
                return False

            l = dfs(node=node.left, min_val=min_val, max_val=node.val)
            r = dfs(node=node.right, min_val=node.val, max_val=max_val)

            return l and r

        return dfs(node=root, min_val=float("-inf"), max_val=float("inf"))
