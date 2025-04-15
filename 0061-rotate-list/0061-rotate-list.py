# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Get size
        size = 1
        end = head
        while end.next:
            end = end.next
            size += 1
        
        k = k % size
        if not k or k == 0:
            return head

        # Locate 
        curr = head
        for _ in range(size - k - 1):
            curr = curr.next
        
        start = curr.next
        curr.next = None
        end.next = head

        return start


