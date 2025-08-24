class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        target = 7, nums = [2,3,1,2,4,3]
                              l
                                    r


                              6 >= 7
        res = min(res, r - l + 1)
        """

        res = float("inf")
        l = 0
        window_sum = 0

        for r in range(len(nums)):
            window_sum += nums[r]

            while l <= r and window_sum >= target:
                res = min(res, r - l + 1)
                window_sum -= nums[l]
                l += 1

        return res if res != float("inf") else 0