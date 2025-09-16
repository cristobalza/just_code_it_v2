class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Binary Search

        find number using it
        then go in both directions to find max and min idx


        """

        def get_min_max_idx(nums, m):
            min_idx, max_idx = m, m

            while max_idx + 1 < len(nums) and nums[max_idx] == nums[max_idx + 1]:
                max_idx += 1

            while 0 <= min_idx - 1 and nums[min_idx - 1] == nums[min_idx]:
                min_idx -= 1

            return min_idx, max_idx


        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                min_idx, max_idx = get_min_max_idx(nums, m)
                return [min_idx, max_idx]

            if nums[l] <= target < nums[m]:
                r = m

            else:
                l = m + 1

        return [-1, -1]