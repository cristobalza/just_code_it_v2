class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        [1, 2, 3]
         i
         j

        Output: 3

        Input: [1, 2, 1]
                i
                      j 

        Min - 1
        Set all occurrences of the minimum to 0

        [0, 2, 0]
            i
            j 

        Min - 2
        Set all occurrences of the minimum to 0

        [0, 0, 0]
            i
            j 

        Output - 2

        Input: [1,2,1,2,1,2]
                          i

        num = 1


        num > 0 
        stack = [1, 2]
        res = 4
        



        """

        stack = []
        res = 0

        for num in nums:
            while stack and stack[-1] > num:
                stack.pop()

            if num > 0:
                if not stack or stack[-1] != num:
                    stack.append(num)
                    res += 1

        return res
        