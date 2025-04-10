class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curr_max, curr_min = 1, 1

        for num in nums:
            old_curr_max = num * curr_max

            curr_max = max(num * curr_max, num * curr_min, num)
            curr_min = min(old_curr_max, num * curr_min, num)

            res = max(res, curr_max)

        return res