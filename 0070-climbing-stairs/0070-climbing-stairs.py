class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dfs(curr_step):
            if curr_step > n:
                return 0
            if curr_step == n:
                return 1
            if curr_step in memo:
                return memo[curr_step]
            
            memo[curr_step] = dfs(curr_step + 1) + dfs(curr_step + 2)

            return memo[curr_step]

        return dfs(1) + dfs(2)
        