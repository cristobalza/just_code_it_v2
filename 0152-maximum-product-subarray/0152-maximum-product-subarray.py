class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """

        nums = [2,3,-2,4]
                       i


       max_value = 6//
       min_value = -8


        dp = [(max, min), (), ()]

        """
        # kadane's

        res = float("-inf")
        max_value, min_value = 1, 1

        for num in nums:
            temp = max_value * num

            max_value = max(max_value * num, min_value * num, num)
            min_value = min(temp           , min_value * num, num)

            res = max(res, max_value)

        return res # O(N) time and O(1) space

        