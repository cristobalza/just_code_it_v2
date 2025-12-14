class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums_counter = collections.Counter(nums)

        missing_num = 0
        repeated_num = 0
        for num in range(1, len(nums) + 1):
            if num not in nums_counter:
                missing_num = num
            if nums_counter[num] > 1:
                repeated_num = num

        return [repeated_num, missing_num]



