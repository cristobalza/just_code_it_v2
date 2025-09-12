class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Input: nums = [3,4,5,1,2]
                       l
                               r
                           m

        """
        
        n = len(nums)
        l, r = 0, n - 1

        while l < r:

            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        return nums[l]