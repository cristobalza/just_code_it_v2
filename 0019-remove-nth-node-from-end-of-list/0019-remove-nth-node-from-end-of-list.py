# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        curr = head
        size = 0

        while curr:
            size += 1
            curr = curr.next
        
        target = size - n
        k = 0 

        dummy = ListNode(-1, head)
        prev, curr = dummy, head
        while curr:
            if k == target:
                prev.next = curr.next
                break
            else:
                k += 1
                prev, curr = curr, curr.next
            
        return dummy.next
        