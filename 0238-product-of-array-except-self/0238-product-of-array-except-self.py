class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """

        nums = [1,2,3,4]
                i


        [1, 1, 2, 6]
        [24, 12, 4, 1]

        [1* 24, 1* 12, 2* 4, 6 * 1]

        """
        n = len(nums)
        prefix, suffix = [1] * n, [1] * n

        for i in range(1, n):
            prefix[i] = nums[i - 1] * prefix[i - 1]

        for i in range(n - 2, -1, -1):
            suffix[i] = nums[i + 1] * suffix[i + 1]

        res = []

        for i in range(n):
            res.append(prefix[i] * suffix[i])

        return res
        