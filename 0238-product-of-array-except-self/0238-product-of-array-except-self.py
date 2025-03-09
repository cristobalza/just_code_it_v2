class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """

                  [1, 2, 3, 4]

    forward_arr   [1, 2, 6, 24]
    backward_arr  [24, 24, 12, 4]


    out [24, 12, 8, 6]


        """

        res = [1] * len(nums)
        forward_arr = [1] * len(nums)
        backward_arr = [1] * len(nums)

        for i in range(1, len(nums)):
            forward_arr[i] = nums[i - 1] * forward_arr[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            backward_arr[i] = nums[i + 1] * backward_arr[i + 1]

        for i in range(len(nums)):
            res[i] = backward_arr[i] * forward_arr[i]

        return res
        