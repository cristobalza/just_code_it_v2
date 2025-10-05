# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node: TreeNode, prev_val: int) -> None:
            nonlocal res

            if not node: 
                return

            if prev_val == float('-inf') or node.val >= prev_val:
                res += 1
            
            prev_val = max(prev_val, node.val)

            dfs(node.left, prev_val)
            dfs(node.right, prev_val)        

            return

        res = 0
        dfs(root, float('-inf'))
        return res