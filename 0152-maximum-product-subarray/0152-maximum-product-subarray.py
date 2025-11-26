class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        max_val, min_val = 1, 1

        res = float("-inf")
        for num in nums:

            curr = max_val * num

            max_val = max(max_val * num, min_val * num, num)
            min_val = min(curr, min_val * num, num)

            res = max(res, max_val, min_val)

        return res
        