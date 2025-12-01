class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        """

        nums = [1,0,0,0,1,0,0,1], k = 2
                        i
          
        last_one = 0
        i = 4
        distance between last_one and i -> i - last_one + 1 - 2 >= k should be approved

        """

        last_one = -1

        for i in range(len(nums)):
            if nums[i] == 1:
                if last_one != -1 and i - last_one - 1 < k:
                    return False
                last_one = i

        return True