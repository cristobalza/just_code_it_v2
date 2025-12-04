# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Get the size
        curr = head
        size = 0
        while curr:
            size += 1
            curr = curr.next
        
        # Reverse function - returns (new_head, new_tail, next_start)
        def reverse_ll(node, k):
            prev = None
            curr = node
            tail = node  # The original head becomes the tail after reversal
            
            for _ in range(k):
                curr.next, prev, curr = prev, curr, curr.next
            
            return prev, tail, curr  # new_head of reversed, new_tail of reversed, start of next group
        
        # Use a dummy node to handle edge cases
        dummy = ListNode(-1, head)
        prev_tail = dummy  # Tail of the previous reversed group
        curr = head
        
        # Reverse groups of k
        while size >= k:
            new_head, new_tail, next_start = reverse_ll(curr, k)
            prev_tail.next = new_head  # Connect previous group to current reversed group
            prev_tail = new_tail       # Update prev_tail for next iteration
            curr = next_start          # Move to start of next group
            size -= k
        
        # Connect the remaining nodes (if any)
        prev_tail.next = curr
        
        return dummy.next