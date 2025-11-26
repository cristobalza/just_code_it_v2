# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Find mid and end (slow fast pointers)
        s, f = head, head
        while f and f.next:
            s = s.next
            f = f.next.next

        mid = s
        # Reverse from mid to end 
        prev = None
        while mid:
            mid.next, mid, prev = prev, mid.next, mid
        
        reverse_curr = prev
        # Merge the start with the reversed ll
        curr = head
        dummy = ListNode(-1, curr)
        while curr.next and reverse_curr.next:
            curr.next, reverse_curr.next, curr, reverse_curr = reverse_curr, curr.next, curr.next, reverse_curr.next
        