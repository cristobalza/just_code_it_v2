# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
                       0 1 2  3
        Input: head = [3,2,0,-4]
                              S 
                              F

        Input: head = [1,2]
                       S
                       F
        """

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                start_cycle_node = head
                while start_cycle_node != fast:
                    start_cycle_node = start_cycle_node.next
                    fast = fast.next
                return start_cycle_node

        return None