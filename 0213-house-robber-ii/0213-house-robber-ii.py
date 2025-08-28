class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 4:
            return max(nums)

        dp_f = [0] * (n - 1)
        dp_f[0] = nums[0]
        dp_f[1] = max(nums[0], nums[1])
        for i in range(2, n - 1):
            dp_f[i] = max(dp_f[i - 1], nums[i] + dp_f[i - 2])

        dp_b = [0] * n
        dp_b[1] = nums[1]
        dp_b[2] = max(nums[1], nums[2])
        for i in range(3, n):
            dp_b[i] = max(dp_b[i - 1], nums[i] + dp_b[i - 2])

        return max(dp_f[-1], dp_b[-1])