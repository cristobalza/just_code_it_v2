# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # get full length
        curr = head 
        lenght = 0
        while curr:
            lenght += 1
            curr = curr.next

        # substract lenght until it reaches n
        dummy = ListNode(-1, head)
        prev, curr = dummy, head

        while curr: 
    
            if lenght == n:
                prev.next, curr = curr.next, curr.next
            else:
                prev, curr = curr, curr.next

            lenght -= 1

        return dummy.next


        