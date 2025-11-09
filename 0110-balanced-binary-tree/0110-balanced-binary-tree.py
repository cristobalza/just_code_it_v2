# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        How to check that a tree is unbalance?
            Number of nodes in left and right -> if abs(r_height - l_height) > 1 then its false

    
        """

        def dfs(node, height, is_balanced) -> [int, bool]:
            if not node:
                return 0, True

            l_h, l_is_balanced = dfs(node.left, height, is_balanced)
            r_h, r_is_balanced = dfs(node.right, height, is_balanced)

            if l_is_balanced is False or r_is_balanced is False:
                return height, False

            if abs(l_h - r_h) > 1:
                is_balanced = False

            return 1 + max(l_h, r_h), is_balanced

        return dfs(root, 0, True)[1]


        