class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        dp = [False] * n
        dp[0] = True

        for i in range(n):

            if dp[i] is False:
                return False

            jump = min(i + nums[i], n - 1)

            for j in range(i + 1, jump + 1):
                dp[j] = True
        
        return dp[-1]
            
        