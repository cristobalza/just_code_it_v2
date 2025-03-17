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

        """

        [1,2,3,4,5]
               s
                     f

        4 -> 5
      r m

        mid.next = reverse
        reverse = mid
        mid = mid.next

        [1,2,3,4,5]
         c   m   

        1 -> 2 => 3
             c
        5 -> 4 reverse second half
             r
        1 -> 5 -> 2 -> 4 -> 3

        find mid
        build reverse from mid
        rebuild

        """
        if not head and not head.next:
            return 

        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow
        reverse = None

        while mid:
            mid.next, reverse, mid = reverse, mid, mid.next

        curr = head
        while curr.next and reverse.next:
            curr.next, reverse.next, reverse, curr = reverse, curr.next, reverse.next, curr.next

        


        