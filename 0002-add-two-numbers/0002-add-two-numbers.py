# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''

        l1 = [2,4,9], l2 = [5,6,4,9]

        942 + 9465 = 10387

        turn the intger into a string
        reverse it
        iterate through it and create new linked list
        '''

        def sum_ll(ll: Optional[ListNode]) -> int:
            ll_vals_list = []

            while ll:
                ll_vals_list.append(str(ll.val))
                ll = ll.next

            return int("".join(ll_vals_list)[::-1])

        l1_sum, l2_sum = sum_ll(l1), sum_ll(l2)

        total_sum = l1_sum + l2_sum

        total_sum_reversed_str = str(total_sum)[::-1]

        dummy = ListNode(-1)
        curr = dummy

        for each_digit in total_sum_reversed_str:
            node = ListNode(val=int(each_digit))
            curr.next = node
            curr = node
        
        return dummy.next