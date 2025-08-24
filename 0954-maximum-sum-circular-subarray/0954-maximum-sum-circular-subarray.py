class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        global_max, global_min, total_sum = nums[0], nums[0], 0
        current_max, current_min = 0, 0

        for num in nums:
            current_max = max(current_max + num, num)
            global_max = max(global_max, current_max)

            current_min = min(current_min + num, num)
            global_min = min(global_min, current_min)

            total_sum += num

        if global_max < 0:
            return global_max

        return max(global_max, total_sum - global_min)
