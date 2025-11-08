class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(i, subset):
            if i == len(nums):
                res.append(nums[::])
                return 

            for j in range(i, len(nums)):

                nums[i], nums[j] = nums[j], nums[i]

                backtrack(i + 1, subset)

                nums[i], nums[j] = nums[j], nums[i]


        res = []

        backtrack(0, nums)

        return res