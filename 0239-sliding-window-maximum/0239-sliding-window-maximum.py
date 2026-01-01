class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        q = collections.deque()
        max_val = float("-inf")
        hmap = {}
        for i in range(k):
            max_val = max(max_val, nums[i])
            q.append(nums[i])
            hmap[nums[i]] = 1 + hmap.get(nums[i], 0)

        res = []
        res.append(max_val)

        for i in range(k, len(nums)):
            pop_val = q.popleft()
            hmap[pop_val] -= 1
            if hmap[pop_val] == 0:
                del hmap[pop_val]
            
            if max_val == pop_val:
                max_val = max(hmap.keys()) if hmap else float("-inf")

            q.append(nums[i])
            hmap[nums[i]] = 1 + hmap.get(nums[i], 0)

            max_val = max(max_val, nums[i])

            res.append(max_val)

        return res
         