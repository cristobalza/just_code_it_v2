# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next

        target = size - n

        curr = head
        dummy = ListNode(-1, head)
        prev = dummy

        while curr and target > 0:
            prev = curr
            curr = curr.next
            target -= 1
        
        prev.next = curr.next

        return dummy.next
        