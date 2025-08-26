class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            print(l)

            if nums[l] > nums[m]:
                r = m
            elif nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        return nums[l]