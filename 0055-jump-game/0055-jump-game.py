class Solution:
    def canJump(self, nums: List[int]) -> bool:
    
        def helper(i):
            if i in memo:
                return memo[i]

            if i == len(nums) - 1:
                return True

            if nums[i] == 0:
                return False

            end = min(len(nums), nums[i] + i + 1)
            
            for j in range(i + 1, end):
                if helper(j):
                    memo[i] = True
                    return True
            memo[i] = False
            return False
            
        memo = {}
        return helper(0)