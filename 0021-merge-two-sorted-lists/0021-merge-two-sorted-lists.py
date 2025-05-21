# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(-1)
        curr = dummy

        while list1 and list2: 
            if list1.val > list2.val:
                new_node = ListNode(list2.val)
                list2 = list2.next
            else:
                new_node = ListNode(list1.val)
                list1 = list1.next

            curr.next = new_node
            curr = curr.next

        if list1:
            curr.next = list1
        else:
            curr.next = list2

        return dummy.next
