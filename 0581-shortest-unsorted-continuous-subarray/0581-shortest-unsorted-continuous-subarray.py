class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = -1, -1
        
        # Find rightmost position where element < max seen so far (from left)
        max_so_far = float('-inf')
        for i in range(n):
            max_so_far = max(max_so_far, nums[i])
            if nums[i] < max_so_far:
                right = i
        
        # Find leftmost position where element > min seen so far (from right)
        min_so_far = float('inf')
        for i in range(n - 1, -1, -1):
            min_so_far = min(min_so_far, nums[i])
            if nums[i] > min_so_far:
                left = i
        
        return 0 if right == -1 else right - left + 1