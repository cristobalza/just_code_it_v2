class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        # maxheap = []

        # for num in set(nums):
        #     heapq.heappush(maxheap, (-num))

        # k = 3

        # res = 0
        # while k > 0:
        #     if maxheap:
        #         res = -1 * heapq.heappop(maxheap)
        #     else:
        #         return max(nums)
        #     k -= 1

        # return res 
        


        minheap = [] # at least 3 values -> O(1) space
        hs = set() # at least 3 values -> O(1) space

        for i in range(len(nums)):
            if nums[i] in hs:
                continue
            
            hs.add(nums[i])
            heapq.heappush(minheap, nums[i])

            if len(minheap) > 3:
                val = heapq.heappop(minheap)
                hs.remove(val)

        if len(minheap) == 3:
            return minheap[0]

        else:
            return max(minheap)
                