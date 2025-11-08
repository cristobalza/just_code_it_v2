class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
         0 1 2 3 4
        [4,1,2,1,2]

        """

        res = nums[0]

        for num in nums[1:]:
            res ^= num

        return res
        