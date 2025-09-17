class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
               

        deque = nums[: k+1] = [1, 3, -1] -> get_max -> 3

        then popleft and append new value

        res = [3]

        """

        # Monotonically decreasing queue
    
        q = collections.deque()

        res = []

        l = 0

        for r in range(len(nums)):

            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            if l > q[0]:
                q.popleft()
                

            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1

        return res

        return res