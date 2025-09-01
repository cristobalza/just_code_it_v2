class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)

        for l in range(n):
            
            if 0 < l and nums[l - 1] == nums[l]:
                continue

            m = l + 1
            r = n - 1

            while m < r:
                curr_sum = nums[l] + nums[m] + nums[r]

                if curr_sum == 0:
                    res.append([nums[l], nums[m], nums[r]])
                    m = m + 1
                    while m < n and m < r and nums[m - 1] == nums[m]:
                        m = m + 1

                elif curr_sum > 0:
                    r = r - 1

                else:
                    m = m + 1

        return res
        
