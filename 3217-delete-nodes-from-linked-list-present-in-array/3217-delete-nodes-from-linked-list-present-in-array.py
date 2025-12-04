# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_set = set(nums)

        dummy = ListNode(-1, head)
        curr = head
        prev = dummy
        
        while curr:
            if curr.val in nums_set:
                # rm the curr node
                curr, prev.next= curr.next, curr.next

            else:
                curr, prev = curr.next, curr

        return dummy.next