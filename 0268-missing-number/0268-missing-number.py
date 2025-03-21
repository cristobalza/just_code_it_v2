class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hashset = set(nums)

        if 0 not in hashset:
            return 0

        for num in nums:
            if num - 1 not in hashset and num - 1 != -1:
                return num - 1
    
        return max(nums) + 1