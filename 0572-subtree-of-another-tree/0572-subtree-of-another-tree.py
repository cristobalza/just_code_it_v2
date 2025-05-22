# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(node, subRoot):
            if not node:
                return False

            if node.val == subRoot.val:
                res = self.is_same_tree(node, subRoot)
                if res:
                    return True
                
            l = dfs(node.left, subRoot)
            r = dfs(node.right, subRoot)

            return l or r

        return dfs(root, subRoot)

    def is_same_tree(self, p, q):
        
        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False

        l = self.is_same_tree(p.left, q.left)
        r = self.is_same_tree(p.right, q.right)

        return l and r
