class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """ 
                0 1 2 3 4
        nums = [1,3,4,2,2]
                    r
                    l
                    

        l=2
        r=2

        m = 2

        pivot = sum(1 for num in nums if num <= m else 0) = 1 + 0 + 0 + 1 + 1 = 3

        pivot = 1 + 0 + 0 + 0 + 0 = 1

            3 <= 2
            1 <= 1
        if pivot <= m: 
            l = m + 1
        else:
            r = m

        """

        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            pivot = sum(1 for num in nums if num <= m)

            if pivot <= m:
                l = m + 1
            else:
                r = m

        return l
