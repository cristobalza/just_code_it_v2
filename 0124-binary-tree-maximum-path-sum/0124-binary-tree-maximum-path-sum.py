# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            nonlocal res

            if not node:
                return 0, res

            l, res = dfs(node.left)
            r, res = dfs(node.right)

            l = max(0, l)
            r = max(0, r)
            
            res = max(res, node.val + l + r)
            
            return node.val + max(l, r), res
            
        res = float("-inf")
        return dfs(root)[1]