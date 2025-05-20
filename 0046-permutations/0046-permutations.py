class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(i, nums):

            if i == len(nums):
                res.append(nums.copy())
                return

            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                backtrack(i + 1, nums)
                nums[i], nums[j] = nums[j], nums[i]
            
            return

        res = []
        backtrack(0, nums)
        return res