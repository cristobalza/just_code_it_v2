class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # kadane's algorithm

        n = len(nums)
        res = [float("-inf")] * n

        curr_sum = 0

        for i, num in enumerate(nums):
            curr_sum += num
            res[i] = curr_sum
        
        return res


        
