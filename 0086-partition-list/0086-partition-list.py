# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        """

        head = [1,4,3,2,5,2], x = 3


        d_s ->  1 -> 2 -> 2
                          s

        d_l -> 4 -> 3 -> 5
                         l

        """

        dummy_small = ListNode(-1)

        smaller_node = dummy_small

        dummy_large = ListNode(-2)

        larger_node = dummy_large

        curr = head
        while curr:
            if curr.val < x:
                smaller_node.next = curr
                smaller_node = curr
                curr = curr.next
            else:
                larger_node.next = curr
                larger_node = curr
                curr = curr.next
                larger_node.next = None

        smaller_node.next = dummy_large.next

        return dummy_small.next

            

        