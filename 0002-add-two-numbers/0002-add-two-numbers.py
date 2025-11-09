# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1_str, num2_str = "", ""

        curr = l1
        while curr:
            num1_str += str(curr.val)
            curr = curr.next

        curr = l2
        while curr:
            num2_str += str(curr.val)
            curr = curr.next

        num1_str, num2_str = num1_str[::-1], num2_str[::-1]

        total_num_str = str(int(num1_str) + int(num2_str))[::-1]

        dummy = ListNode(-1)
        curr = dummy
        for digit_str in total_num_str:
            curr.next = ListNode(val=int(digit_str))
            curr = curr.next

        return dummy.next

