class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        def dfs(i, target):
            # Base cases
            if target == 0:
                return True
            if i >= len(nums) or target < 0:
                return False
            
            # Check memo with (i, target) as key
            if (i, target) in memo:
                return memo[(i, target)]
            
            # Try including or excluding current number
            memo[(i, target)] = dfs(i + 1, target - nums[i]) or dfs(i + 1, target)
            
            return memo[(i, target)]
        
        memo = {}
        return dfs(0, sum(nums) // 2)