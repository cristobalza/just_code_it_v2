# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            # Base case: empty node has height 0 and is balanced
            if not node:
                return 0, True
            
            # Get height and balance status of left subtree
            left_height, left_balanced = dfs(node.left)
            if not left_balanced:
                return -1, False
                
            # Get height and balance status of right subtree
            right_height, right_balanced = dfs(node.right)
            if not right_balanced:
                return -1, False
            
            # Check if current node is balanced
            height_diff = abs(left_height - right_height)
            is_balanced = height_diff <= 1
            
            # Current node's height is 1 + max of subtree heights
            current_height = 1 + max(left_height, right_height)
            
            return current_height, is_balanced
        
        _, is_balanced = dfs(root)
        return is_balanced