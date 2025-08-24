# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        """
        ith node is twin with the (n-1-i)th node --> i <==> (n-1-i)
                
        all nodes can have twin ndoes??
                0 1 2 3
        head = [5,4,2,1]

        node = 0 => twin node = (4 - 1 - 0) = 3 *
        node = 1 => twin node = (4 - 1 - 1) = 2 **
        node = 2 => twin node = (4 - 1 - 2) = 1 **
        node = 3 => twin node = (4 - 1 - 3) = 0 *

        store in a list as iterate through the ll
        then iterate through the list to calculate the sum of the node + twin and store in a variable
        """

        curr = head
        n = 0
        node_list = []
        while curr:
            n += 1
            node_list.append(curr.val)
            curr = curr.next
        
        res = 0
        for i in range(n):
            node_val = node_list[i]
            twin_node_val = node_list[n - 1 - i]
            res = max(res, node_val + twin_node_val)

        return res