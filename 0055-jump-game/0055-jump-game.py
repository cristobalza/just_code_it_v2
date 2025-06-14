class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        def helper(i):
            
            if i in memo:
                return memo[i]

            if i >= (n - 1):
                memo[i] = True
                return True

            if nums[i] == 0:
                memo[i] = False
                return False

            jump = min(i + nums[i], n - 1) # keep in bound for the iteration

            for j in range(i + 1, jump + 1):
                if helper(j):
                    memo[i] = True
                    return True

            memo[i] = False
            return False
            
        n = len(nums)
        memo = {}
        return helper(0)