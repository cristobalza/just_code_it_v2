class Solution:
    def canJump(self, nums: List[int]) -> bool:

        def dfs(i):

            if i in memo:
                return memo[i]
            
            if i == n - 1:
                return True

            if nums[i] == 0:
                return False

            jump_upper_bound = min(i + nums[i], n - 1)

            for j in range(jump_upper_bound, i, -1):
                if dfs(j):
                    memo[i] = True
                    return True
            memo[i] = False
            return False

        memo = {}
        n = len(nums)

        return dfs(0)