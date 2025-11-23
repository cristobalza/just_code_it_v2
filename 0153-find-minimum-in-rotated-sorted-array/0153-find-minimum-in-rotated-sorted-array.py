class Solution:
    def findMin(self, nums: List[int]) -> int:

        """
        nums = [3,4,5,1,2]
                l.      r
                    m


        if l < m:
            if m < r:
                r = m
            else:
                l = m + 1
        else:
            if m < r:
                r = m
            else:
                l = m + 1
        """
        
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[l] <= nums[m]:
                if nums[m] > nums[r]:
                    l = m + 1

                else:
                    r = m

            else:
                if nums[m] < nums[r]:
                    r = m
                else:
                    l = m + 1

        return nums[l]