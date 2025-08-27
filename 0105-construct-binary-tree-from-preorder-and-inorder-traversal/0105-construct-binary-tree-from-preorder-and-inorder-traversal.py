# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def dfs(preorder, inorder):

            if not preorder or not inorder:
                return None

            val = preorder.pop(0)

            node = TreeNode(val=val)
            inorder_idx = inorder.index(val)

            node.left = dfs(preorder, inorder[:inorder_idx])
            node.right = dfs(preorder, inorder[inorder_idx + 1:])

            return node

        return dfs(preorder, inorder)