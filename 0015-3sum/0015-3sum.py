class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for l in range(len(nums)):
            # Skip the adjacent values
            if l > 0 and nums[l - 1] == nums[l]:
                continue
            
            m = l + 1
            r = len(nums) - 1

            while m < r:
                curr = nums[l] + nums[m] + nums[r]

                if curr < 0:
                    m += 1
                elif curr > 0:
                    r -= 1
                else:
                    res.append([nums[l], nums[m], nums[r]])
                    m += 1
                    
                    # Skip the adjacent values
                    while m < r and m < len(nums) and nums[m - 1] == nums[m]:
                        m += 1


        return res                    
