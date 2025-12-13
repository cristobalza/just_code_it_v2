# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """

        Given
            head - linked list
            n - lenght of head

        Delete the middle node (n // 2)th 

        What is x?

        Slow and fast pointers for even and odd size lists

        [1,3,4,7,1,2,6]
             p
               s
                     f

        prev.next = slow.next


        Input: head = [1,2,3,4]
                           s
                                 f


        """
        slow, fast = head, head
        dummy = ListNode(-1, head)
        prev = dummy

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next

        return dummy.next