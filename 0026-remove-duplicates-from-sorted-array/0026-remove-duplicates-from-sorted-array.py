class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Input: nums = [0,1,2,3,4,2,2,3,3,4]
                               l
                                          r
        
        if r - 1 and r are differnet
            set l to r
            l ++

        """

        l = 1

        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1

        return l
