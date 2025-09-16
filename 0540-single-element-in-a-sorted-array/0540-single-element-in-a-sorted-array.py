class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
                       0 1 2 3 4 5 6 7 8
        Input: nums = [1,1,2,3,3,4,4,8,8]
                       l
                            r 
                       m

                        m = 1 which is even, let's substrac 1
                        nums[m] != nums[m + 1]
                            r = m
        binary search

    
        """

        n = len(nums)
        l, r = 0, n - 1

        while l < r:

            m = (l + r) // 2

            if (0 <= m - 1 and nums[m - 1] != nums[m]) and (m + 1 < n and nums[m] != nums[m + 1]):
                return nums[m]

            if m % 2 != 0:
                m -= 1
            
            
            if m + 1 < n and nums[m] == nums[m + 1]:
                l = m + 2
            else:
                r = m


        return nums[l]
                
        