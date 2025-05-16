class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def backtrack(i, subset):
            nonlocal res

            if i == len(nums):
                res.append(subset[:])
                return

            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            backtrack(i + 1, subset)

            return

        res = []

        backtrack(0, [])

        return res
            

        