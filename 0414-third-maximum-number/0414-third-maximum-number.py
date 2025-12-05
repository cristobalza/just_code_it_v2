class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        maxheap = []

        for num in set(nums):
            heapq.heappush(maxheap, (-num))

        k = 3

        res = 0
        while k > 0:
            if maxheap:
                res = -1 * heapq.heappop(maxheap)
            else:
                return max(nums)
            k -= 1

        return res 
        