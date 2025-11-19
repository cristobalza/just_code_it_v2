# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(node):

            if not node:
                return False

            if node.val == subRoot.val:
                if compare_dfs(node, subRoot):
                    return True
            
            l = dfs(node.left)
            r = dfs(node.right)

            return l or r

        def compare_dfs(node, subRoot):
            if not node and not subRoot:
                return True

            if (not node or not subRoot) or (node.val != subRoot.val):
                return False

            return compare_dfs(node.left, subRoot.left) and compare_dfs(node.right, subRoot.right)

        return dfs(root)