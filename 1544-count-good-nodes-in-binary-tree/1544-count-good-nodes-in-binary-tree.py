# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, prev_val):
            if not node: 
                return 0

            l = dfs(node.left, max(node.val, prev_val))
            r = dfs(node.right, max(node.val, prev_val))

            return 1 + l + r if prev_val <= node.val else l + r


        return dfs(root, float("-inf"))
        