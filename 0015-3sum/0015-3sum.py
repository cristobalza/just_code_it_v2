class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []

        nums.sort()

        for i, num in enumerate(nums):

            if i > 0 and nums[i - 1] == num:
                continue
            
            m, r = i + 1, len(nums) - 1

            while m < r:
                total = num + nums[m] + nums[r]

                if total > 0:
                    r -= 1
                elif total < 0:
                    m += 1
                else:
                    res.append([num, nums[m], nums[r]])
                    m += 1

                    while m < r and nums[m - 1] == nums[m]:
                        m += 1

        return res