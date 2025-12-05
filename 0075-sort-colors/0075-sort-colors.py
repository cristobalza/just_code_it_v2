class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
         nums = [0,2,2,1,1,0]
                   i
                           j
                 k

                [0,0,1,1,2,2]
                     i.          for 0
                         i           for 1
                            j

        szie = 6

        count_0 = 2
        count_1 = 2

        [0 - count_0
                   count_0 + 1       count_0 + count_1
                                                       count_0 + count_1 + 1
                                                                                      n- 1]



        """

        count_0, count_1, count_2 = 0, 0 ,0

        for num in nums:
            if num == 0:
                count_0 += 1
            elif num == 1:
                count_1 += 1
            else:
                count_2 += 1

        for i in range(len(nums)):
            if 0 <= i < count_0:
                nums[i] = 0
            elif count_0 <= i < count_0 + count_1:
                nums[i] = 1
            else:
                nums[i] = 2
            

        

            



        

            

        
                
        

