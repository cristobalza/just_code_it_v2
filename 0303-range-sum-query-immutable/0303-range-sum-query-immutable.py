class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0] * (len(nums) + 1)
        self.prefix[0] = nums[0]
        for i in range(1, len(nums)):
            self.prefix[i] = self.prefix[i - 1] + nums[i]
 
    def sumRange(self, left: int, right: int) -> int:
        left_sum = self.prefix[left - 1] if left - 1 >= 0 else 0
        right_sum = self.prefix[right]
        return right_sum - left_sum

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)