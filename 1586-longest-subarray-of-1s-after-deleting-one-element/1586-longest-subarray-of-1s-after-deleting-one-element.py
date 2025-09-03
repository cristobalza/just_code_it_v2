class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
                       0 1 2 3 4 5 6 7 8
        Input: nums = [0,1,1,1,0,1,1,0,1]
                         l
                                  r 

        zero_count = 2

        window_size = r - l + 1 = 2- 0 + 1 = 3
  
             2 > 1 and  3 
        while zero_count > 1 and window_size - zero_count > 1
            l += 1
            if zero_count >= 0
                zero_count -= 1

        """

        l = 0
        res = 0
        zero_count = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[l] == 0:
                    zero_count -= 1
                
                l += 1
            
            res = max(res, r - l + 1 - 1) # delete the element from it

        return res
        