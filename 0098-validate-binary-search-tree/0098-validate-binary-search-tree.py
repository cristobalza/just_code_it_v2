# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return None, None, True # min, max, is valid BST

            l_min, l_max, l_valid = dfs(node.left)

            if not l_valid or (l_max is not None and node.val <= l_max):
                return None, None, False

            r_min, r_max, r_valid = dfs(node.right)

            if not r_valid or (r_min is not None and node.val >= r_min):
                return None, None, False

            curr_min = l_min if l_min is not None else node.val
            curr_max = r_max if r_max is not None else node.val

            return curr_min, curr_max, True

        return dfs(root)[2]