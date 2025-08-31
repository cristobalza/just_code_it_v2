class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        dp = [1] * n

        for l in range(n - 1, -1, -1):
            for r in range(l + 1, n):
                if nums[l] < nums[r]:
                    dp[l] = max(dp[l], 1 + dp[r])

        return max(dp)



        