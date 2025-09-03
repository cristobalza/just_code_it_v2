class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        curr_sum = sum(nums[:k])
        max_avg = curr_sum / k
        
        # Slide the window: remove leftmost, add rightmost
        for i in range(k, len(nums)):
            curr_sum = curr_sum - nums[i - k] + nums[i]
            max_avg = max(max_avg, curr_sum / k)
        
        return max_avg