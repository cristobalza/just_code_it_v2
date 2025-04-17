# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        curr = head
        size = 1
        while curr.next:
            curr = curr.next
            size += 1
        
        target = size - n
        dummy = ListNode(-1, head)
        prev, curr = dummy, head

        k = 0
        while curr:
            if k == target:
                prev.next, curr = curr.next, curr.next

            else:
                prev, curr = curr, curr.next
            k += 1

        return dummy.next
        