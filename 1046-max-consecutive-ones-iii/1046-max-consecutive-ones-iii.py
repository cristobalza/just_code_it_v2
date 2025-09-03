class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """ 
                       0 1 2 3 4 5 6 7 8 9 10
        Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
                                 l
                                           r

        
        total_size_window = r - l + 1 = 10 - 4 + 1 = 7
        max_freq = max(max_freq, hmap[nums[r]]) = max(3, 4) = 4


            7 - 4 = 3 > 2
        if total_size_window - max_freq > k
            hmap[nums[l]] -= 1
            l ++
        

        hmap -> nums[i] value : frequency
        {
            1: 4
            0: 2
        }

        res = max(6, 10 - 5 + 1) = 6
        res = max(res, r - l + 1)


        """
        l = 0
        res = 0
        zero_count = 0
        

        for r in range(len(nums)):
            if nums[r] == 0:
                zero_count += 1

            if zero_count > k:
                if nums[l] == 0:
                    zero_count -= 1
                l += 1

            res = max(res, r - l + 1)

        return res