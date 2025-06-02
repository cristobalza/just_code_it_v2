# Bottom up
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(i):

            if i >= n:
                return 0

            if memo[i] != float("inf"):
                return memo[i]

            memo[i] = max(helper(i + 1), nums[i] + helper(i + 2))

            return memo[i]

        n = len(nums)
        memo = [float("inf")] * (n)
        
        return helper(0)

        
        