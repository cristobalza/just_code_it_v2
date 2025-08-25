class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0] * (len(nums))
        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] + nums[i]
        
        reversed_prefix = [0] * (len(nums))
        reversed_prefix[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            reversed_prefix[i] = reversed_prefix[i + 1] + nums[i]
        
        for i in range(len(nums)):
            if reversed_prefix[i] == prefix[i]:
                return i
        
        return -1