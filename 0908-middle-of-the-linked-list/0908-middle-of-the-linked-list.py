# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        calculate the size of the LL
        if odd then get size // 2 LL
        else then get (size // 2) + 1 LL 

        """

        curr = head
        size = 0
        while curr:
            size += 1
            curr = curr.next
        
        target_node = size // 2
        
        curr = head
        idx = 0
        while idx < size:
            if idx == target_node:
                return curr
            curr = curr.next
            idx += 1