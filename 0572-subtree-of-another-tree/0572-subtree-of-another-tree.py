# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def dfs_subtree(node, subRoot):
            if not node and not subRoot:
                return True
            
            if not node or not subRoot or node.val != subRoot.val:
                return False
            
            return dfs_subtree(node.left, subRoot.left) and dfs_subtree(node.right, subRoot.right)

        
        def dfs(node):
            if not node:
                return False

            if node.val == subRoot.val:
                temp = dfs_subtree(node, subRoot)
                if temp:
                    return True

            return dfs(node.left) or dfs(node.right)

        return dfs(root)
            