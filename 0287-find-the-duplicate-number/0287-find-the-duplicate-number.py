class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Given nums := List[int] - n + 1 integers and each integer is in the range [1, n]

        Only one repeated num in nums - R: this repeated integer

        nums = [1,3,4,2,2]
        Approach 1: get the Counter of each value and return the key that its value is > 1
        O(N) time, O(N) space

        Approach 2:
        Use pointers 

                 0  1  2  3 4
        nums = [-1,-3,-4,-2,2]
                            i

                idx = abs(num[i]) - 1 = 1 - 1 = 0
                idx = abs(num[i]) - 1 = 3 - 1 = 2
                idx = abs(-4) - 1 = 3
                idx = abs(-2) - 1 = 1
                idx = abs(2) - 1 = 1
                
        """
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                return abs(num)
            nums[idx] *= -1 
