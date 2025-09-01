class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
        Input: nums = [1,2,3,4,0]
                                 i
                                 k
                        
        Input: nums = [1,3,12,0,0]
                       i
                              k

                       if k + 1 <= len(nums) and nums[k] == 0 and nums[k+1] != 0:
                            swap nums[k] and nums[k+1]

        """
        
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 0:
                k = i
                while k + 1 < len(nums) and nums[k] == 0 and nums[k + 1] != 0:
                    nums[k], nums[k+1] = nums[k+1], nums[k]
                    k += 1
        

                