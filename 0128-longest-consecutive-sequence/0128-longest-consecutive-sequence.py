class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """

        [100,4,200,1,3,2]
         

        hs =  [100, 4, 200, 1, 3, 2]


        """

        nums_set = set(nums)
        res = 0

        for num in nums_set:
            if (num - 1) not in nums_set:
                curr_lenght = 1
                while (num + curr_lenght) in nums_set:
                    curr_lenght += 1
                res = max(res, curr_lenght)
        return res
