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
            curr = curr.next
            size += 1

        target = size - n

        node_idx = 0
        curr = head
        dummy =  ListNode(-1, curr)
        prev = dummy

        while curr:
            if node_idx == target:
                prev.next = curr.next
                curr = curr.next
                node_idx += 1
            else:
                prev = curr
                curr = curr.next
                node_idx += 1

        return dummy.next