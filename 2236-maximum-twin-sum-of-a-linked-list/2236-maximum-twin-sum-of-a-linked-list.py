# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        """
        ith node is twin with the (n-1-i)th node --> i <==> (n-1-i)
                
        all nodes can have twin ndoes??
                0 1 2 3
        head = [5,4,2,1]

        node = 0 => twin node = (4 - 1 - 0) = 3 *
        node = 1 => twin node = (4 - 1 - 1) = 2 **
        node = 2 => twin node = (4 - 1 - 2) = 1 **
        node = 3 => twin node = (4 - 1 - 3) = 0 *

        store in a list as iterate through the ll
        then iterate through the list to calculate the sum of the node + twin and store in a variable
        O(N) time
        O(N) space

                0 1  | 2 3
        head = [5,4, | 2,1]
                <-     ->)

        n = 4; n // 2 = 4 // 2 = 2

        res = max(res, prev.val + forward.val)

        slow and fast -> use the slow pointer to get the middle (forward)
        as we iterate through it, change pointer direction to backwards

        head = [5,4,2,1]
                S
                    F
                  T
              P
                
                  

        """

        # slow fast
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        res = 0
        while prev and slow:
            res = max(res, prev.val + slow.val)
            prev = prev.next
            slow = slow.next

        return res
