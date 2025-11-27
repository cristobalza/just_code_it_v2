class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float("-inf")

        max_v, min_v = 1, 1

        for num in nums:
            curr = max_v * num

            max_v = max(max_v * num, min_v * num, num)
            min_v = min(curr, min_v * num, num)

            res = max(max_v, res, num)

        return res