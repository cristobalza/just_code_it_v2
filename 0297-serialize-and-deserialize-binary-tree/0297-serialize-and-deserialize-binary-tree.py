# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def dfs(node):
            if not node:
                res.append("N")
                return

            res.append(str(node.val))

            dfs(node.left)
            dfs(node.right)

            return

        res = []
        dfs(root)
        return ",".join(res)



        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        def dfs():
            nonlocal i
            if i >= len(data) or data[i] == "N":
                i += 1
                return None

            node = TreeNode(int(data[i]))
            i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        data = data.split(",")
        i = 0
        return dfs()

            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))