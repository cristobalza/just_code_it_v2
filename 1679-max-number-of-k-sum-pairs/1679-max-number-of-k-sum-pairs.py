class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """

        [3,1,3,4,3]
             l     
                 r

        k = 6
         curr = 4
         res = 1

        """
        nums.sort()

        l, r = 0, len(nums) - 1

        res = 0 # count

        while l < r:
            curr = nums[l] + nums[r]

            if curr == k:
                res += 1
                l += 1
                r -= 1

            elif curr < k:
                l += 1

            else:
                r -= 1


        return res


