class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid
        return r if nums[r] == target else -1
        
        