class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # Sliding Window O(nlogn)
        # nums[r] * (r - l + 1) = "What the sum WOULD BE if all elements were equal to the target"
        # curr_sum = "What the sum ACTUALLY IS right now"
        # The difference = operations needed!
        # While the operations needed is greater than k, the window is too expensive, so shrink it!"

        nums.sort()
        res = 0
        n = len(nums)
        l = 0
        curr_sum = 0

        for r in range(n):
            curr_sum += nums[r]

            while nums[r] * (r - l + 1) - curr_sum > k:
                curr_sum -= nums[l]
                l += 1

            res = max(res, r - l + 1)

        return res

