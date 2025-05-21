# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        minheap = []

        for _linkedlist in lists:
            curr = _linkedlist
            while curr:
                heapq.heappush(minheap, curr.val)
                curr = curr.next

        dummy = ListNode(-1)
        prev = dummy

        while minheap:
            val = heapq.heappop(minheap)

            curr = ListNode(val)

            prev.next = curr
            prev = curr

        return dummy.next
