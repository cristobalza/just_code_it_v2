# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(-1)
        curr = dummy

        l = list1
        r = list2

        while l and r:
            if l.val <= r.val:
                curr.next, l, curr = l, l.next, l
            else:
                curr.next, r, curr = r, r.next, r

        if l is None:
            curr.next = r
        else:
            curr.next = l
        
        return dummy.next




        