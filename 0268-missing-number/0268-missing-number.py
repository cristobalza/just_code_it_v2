class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """            
                       0 1 2
        Input: nums = [3,0,1]
                       i

        size = 3

        i = 0
        nums[i] = 3

        size = 3 - 0 + 3 = 0

        i = 2
        nums[i] = 1

        size = 0 - (0-1) = 1

        i = 1
        nums[i] = 0

        size = 1 - (0 - 1) = 2

        """

        size = len(nums)

        for i in range(len(nums)):
            size += i - nums[i]

        return size
        