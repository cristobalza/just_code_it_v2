class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_idx_dict = {}

        for i, num in enumerate(nums):
            if target - num in num_idx_dict:
                return [num_idx_dict[target - num], i]
            
            num_idx_dict[num] = i
        
        