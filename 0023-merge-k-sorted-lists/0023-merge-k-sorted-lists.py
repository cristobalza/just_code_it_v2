# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        curr = lists[0]
        dummy = ListNode(-1, curr)

        for i in range(1, len(lists)):
            new_linkedlist = lists[i]
            curr = self.mergeTwoLinkedLists(curr, new_linkedlist)
        
        return curr


        
    def mergeTwoLinkedLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(-1)
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                new_node = ListNode(l1.val)
                l1 = l1.next
            else:
                new_node = ListNode(l2.val)
                l2 = l2.next
            
            curr.next = new_node
            curr = curr.next
        
        if l1:
            curr.next = l1
        else:
            curr.next = l2

        return dummy.next