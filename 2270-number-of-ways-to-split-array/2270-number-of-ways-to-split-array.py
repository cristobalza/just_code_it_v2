class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        """
        Given
            nums - list of integers that contains valid split at index i if 
                1. the sum of the first i+1 elements >= sum of the last n - i -1
                2. the is at least one element to the right of i - 0 <= i < n - 1

        Return
            integer that contains the number of splits from above criteria
        """

        n = len(nums)

        total_sum = sum(nums)

        curr_sum = 0

        res = 0

        for i, num in enumerate(nums):
            curr_sum += num
            residual_sum = total_sum - curr_sum
            if i < n - 1 and curr_sum >= residual_sum:
                res += 1

        return res
