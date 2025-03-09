class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        subtrahend_dict = {}
        for i, num in enumerate(nums):
            if target - num in subtrahend_dict:
                return [i, subtrahend_dict[target - num]]
            else:
                subtrahend_dict[num] = i