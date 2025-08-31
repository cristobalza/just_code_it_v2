class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """

        nums = [1,2,2]
                    l
                      r
    
        return l

        nums = [0,1,2,3,4,2,2,3,3,4]
                          l.  
                                  r 
                
        """
        l = 1

        for r in range(1, len(nums)):
            if nums[r - 1] != nums[r]:
                nums[l] = nums[r]
                l += 1
        return l