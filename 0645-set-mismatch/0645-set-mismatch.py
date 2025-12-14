class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup_num, miss_num = 0, 0

        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                dup_num = abs(num)
            else:
                nums[idx] *= -1

        for i in range(len(nums)):
            if nums[i] > 0: 
                miss_num = i + 1

        return [dup_num, miss_num]
