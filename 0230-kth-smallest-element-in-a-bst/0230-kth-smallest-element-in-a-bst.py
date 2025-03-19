# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def dfs(node):
            nonlocal arr, res

            if not node:
                return

            dfs(node.left)
            arr.append(node.val)
            if len(arr) == k:
                res = node.val
                return 
            dfs(node.right)

            return
        
        arr = []
        res = 0
        dfs(root)
        return res