class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
                        l
                             r

        curr_sum = -1


        output: 6
        """

        res = float("-inf")
        curr_sum = 0

        for num in nums:
            curr_sum += num
            res = max(res, curr_sum)
            if curr_sum < 0:
                curr_sum = 0

        return res
        