# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge_linked_lists(l1, l2):
            dummy = ListNode(-1)
            curr = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    curr.next, l1 = l1, l1.next
                else:
                    curr.next, l2 = l2, l2.next

                curr = curr.next

            if l1:
                curr.next = l1
            else:
                curr.next = l2
            
            return dummy.next


        if not lists:
            return None
            
        curr = lists[0]

        for i in range(1, len(lists)):
            nxt = lists[i]

            curr = merge_linked_lists(curr, nxt)

        return curr