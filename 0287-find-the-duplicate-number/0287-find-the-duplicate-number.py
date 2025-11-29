class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l) // 2

            pivot = sum(1 for num in nums if num <= m)

            if pivot <= m:
                l = m + 1

            else:
                r = m

        return l
                