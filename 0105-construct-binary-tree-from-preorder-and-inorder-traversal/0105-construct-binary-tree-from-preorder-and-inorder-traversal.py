# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
         preorder = [3,9,20,15,7], inorder = [9,| 3 | ,15,20,7]
                       i                      l-- i.  ----r

        """

        def dfs(i, inorder):
            if i == len(preorder):
                return None
            
            if not inorder:
                return None

            val = preorder[i]
            node = TreeNode(val)
            idx = inorder.index(val)

            node.left = dfs(i + 1, inorder[:idx])
            node.right = dfs(i + 1 + idx, inorder[idx+1:])

            return node

        return dfs(0, inorder)
