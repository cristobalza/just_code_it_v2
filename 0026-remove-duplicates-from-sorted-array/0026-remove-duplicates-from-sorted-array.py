class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Input: nums = [0,1,2,1,1,0,2,3,3,4]
                           l
                                   r
        
        if l and r are differnet
            l++
            swap l and r values 

        r ++
        """

        l = 1

        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1

        return l
