class Solution:
    def maxProduct(self, nums: List[int]) -> int:   

        dp = [(0, 0) for i in range(len(nums))]

        dp[0] = (nums[0], nums[0])

        for i in range(1, len(nums)):

            max_val = max(nums[i], dp[i-1][0] * nums[i], dp[i-1][1] * nums[i])

            min_val = min(nums[i], dp[i-1][0] * nums[i], dp[i-1][1] * nums[i])

            dp[i] = (max_val, min_val)

        return max(dp)[0]
        