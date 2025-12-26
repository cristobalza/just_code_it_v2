# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """

        head = [1,2,3,4,5], k = 2
                    c
            D
            p.  

          d->  [3, 2, 1] 
                p     t

            p.next, tail = reverse_ll(p.next, curr)
            curr = tail.next


        count = 3

        def reverse_ll(start, end):
            prev = None
            curr = start
            tail = start

            while curr != end:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            return prev, tail # head of reverse ll , end of new reverse ll


        """

        def reverse_ll(start, end):
            prev = None
            curr = start
            tail = start

            while curr != end:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            return prev, tail # head of reverse ll , end of new reverse ll

        
        dummy = ListNode(-1, head)
        prev_global = dummy

        curr = head

        count = 1

        while curr:

            if count % k == 0:
                
                # Set start and end
                start_node = prev_global.next
                next_node = curr.next

                # Reverse ll
                new_head, new_tail = reverse_ll(start_node, next_node)

                # Connect new head and the new tail to the next node
                prev_global.next = new_head
                new_tail.next = next_node

                # Update iteration
                prev_global = new_tail
                curr = next_node


            else:
                curr = curr.next
                
            count += 1

        return dummy.next