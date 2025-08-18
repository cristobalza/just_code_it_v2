class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(subset, i):

            if i == n:
                res.append(subset.copy())
                return

            for j in range(i, n):
                nums[i], nums[j] = nums[j], nums[i]
                backtrack(nums, i + 1)
                nums[i], nums[j] = nums[j], nums[i]

            return

        n = len(nums)
        res = []
        backtrack(nums, 0)
        return res

        