class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Memoization

        def dfs(i, curr):
            
            # Base case
            if i >= len(nums):
                return 1 if curr == target else 0

            if (i, curr) in memo:
                return memo[(i, curr)]

            # Recursion call: try to include +1 and -1
            memo[(i, curr)] = (
                dfs(i + 1, curr + nums[i]) 
                + dfs(i + 1, curr - nums[i])
            )

            return memo[(i, curr)]
        
        memo = {}
        return dfs(0, 0)
        