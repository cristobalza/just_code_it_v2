# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        243 + 564 = 807 => 708
        """
        num1, num2 = "", ""
        c1, c2 = l1, l2

        while c1:
            num1 += str(c1.val)
            c1 = c1.next

        while c2:
            num2 += str(c2.val)
            c2 = c2.next

        total_reversed_str = str(int(num1[::-1]) + int(num2[::-1]))[::-1]

        dummy = ListNode(-1)
        curr = dummy

        for val in total_reversed_str:
            node = ListNode(val=int(val))
            curr.next = node
            curr = curr.next
        
        return dummy.next
