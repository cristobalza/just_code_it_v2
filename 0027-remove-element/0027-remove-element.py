class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Input: nums = [0,1,3,0,4,0,4,2], val = 2
                                 k
                                     i  


        if nums[i] != val:
            nums[k] = nums[i]
            k++
        """
        k = 0

        for num in nums:
            if num != val:
                nums[k] = num
                k += 1
        
        return k
        