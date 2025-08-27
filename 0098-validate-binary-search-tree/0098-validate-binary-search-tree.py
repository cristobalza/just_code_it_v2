# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, all_min, all_max):

            if not node:
                return True

            if node.val <= all_min or node.val >= all_max:
                return False

            l = dfs(node=node.left, all_min=all_min, all_max =node.val)
            r = dfs(node=node.right, all_min=node.val, all_max=all_max)

            return l and r


        return dfs(node=root, all_min=float("-inf"), all_max=float("inf"))
        
        