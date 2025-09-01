class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Run binary search to locate the value
        Then create left and right pointers to travers outwards to find the latest index of that value

        """
        def calculate_max_min_idxs(nums, n, idx):
            val = nums[idx]
            min_idx, max_idx = idx, idx

            while 0 <= min_idx - 1 and nums[min_idx - 1] == val:
                min_idx -= 1

            while max_idx + 1 < n and nums[max_idx + 1] == val:
                max_idx += 1

            return min_idx, max_idx

        n = len(nums)
        l, r = 0, n - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                min_idx, max_idx = calculate_max_min_idxs(nums, n, m)
                return [min_idx, max_idx]
            
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return [-1, -1]
         