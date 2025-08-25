class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
Input: nums = [1,2,3,2,2,3]
                     l 
                         r
    
    l = 1
    for r in range(1, n):
        if nums[r] != nums[r - 1]:
            nums[l] = r
            l ++ 
    return l

Input: nums = [1,1,2,2,3,3]
                       l
                         r

               if i + 2 < n and nums[i+2 ] = nums[l]
                l= i + 2

        """

        l = 2
        n = len(nums)
        for r in range(2, n):
            if nums[r] != nums[l - 2]:
                nums[l] = nums[r]
                l += 1
        return l
        