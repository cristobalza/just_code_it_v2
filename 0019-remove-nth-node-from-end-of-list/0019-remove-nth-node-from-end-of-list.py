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
        
        target = size - n + 1

        curr = head
        dummy = ListNode(-1, curr)
        prev = dummy
        while curr and target > 0:
            
            target -= 1

            if target == 0:
                prev.next, curr = curr.next, curr.next
            else:
                curr, prev = curr.next, curr

        return dummy.next


