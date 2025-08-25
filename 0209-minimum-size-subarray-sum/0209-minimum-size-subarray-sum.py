class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        nums := List[int]
        - positive integes

        target:= int
        - positive int

        R: minimal lenght of a subarray whose sum >= target

        Input: target = 7, nums = [2,3,1,2,4,3]
                                           l
                                               r

                                     4 + 3 >= target = 7

                                    res = 2

        sliding window
        """

        l, r = 0, 0
        res = float("inf")
        curr = 0

        while r < len(nums):
            curr += nums[r]

            while l <= r and curr >= target:
                res = min(res, r - l + 1)
                curr -= nums[l]
                l += 1
            
            r += 1

        return res if res != float("inf") else 0