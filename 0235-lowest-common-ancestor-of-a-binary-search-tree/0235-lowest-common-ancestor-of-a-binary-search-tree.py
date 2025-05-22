# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node, p, q):
            if not node:
                return None

            # Catch the ancestor of itself
            if node.val == p.val or node.val == q.val:
                return node

            l = dfs(node.left, p, q)
            r = dfs(node.right, p, q)

            # Catch the split ancestor
            return node if l and r else l or r

        return dfs(root, p, q)