# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def dfs(q_preorder, inorder):
            # Base case
            if not q_preorder or not inorder:
                return 

            val = q_preorder.popleft()
            node = TreeNode(val)
            i = inorder.index(val)

            # Recursive call
            node.left = dfs(q_preorder, inorder[:i])
            node.right = dfs(q_preorder, inorder[i + 1:])

            return node

        q = collections.deque(preorder)
        return dfs(q, inorder)

