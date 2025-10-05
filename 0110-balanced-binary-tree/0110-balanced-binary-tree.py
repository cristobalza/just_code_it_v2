# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(node, curr_height, is_balanced):
            if not node:
                return 0, True

            l_height, l_balanced = dfs(node.left, curr_height, is_balanced)
            if l_balanced is False:
                return curr_height, False

            r_height, r_balanced = dfs(node.right, curr_height, is_balanced)
            if r_balanced is False:
                return curr_height, False

            if abs(r_height - l_height) > 1:
                is_balanced = False

            return 1 + max(l_height, r_height), is_balanced

        _, res = dfs(root, 0, True)

        return res
