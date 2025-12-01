class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        """
        nums = [1,2,3]

        i = 0
        nums[i] = 1
        if nums[i] == 

        """

        res = float("inf")

        for i in range(len(nums)):
            curr = 0
            num = nums[i]
            while num > 0:
                curr += num % 10

                num = num // 10

            if curr == i:
                res = min(res, curr)

        return res if res != float("inf") else -1

        