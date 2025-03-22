class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for left in range(len(nums)):
            if left > 0 and nums[left] == nums[left - 1]:
                continue
            mid, right = left + 1, len(nums) - 1
            
            while mid < right:
                temp = nums[left] + nums[mid] + nums[right]
                
                if temp == 0:
                    res.append([nums[left] , nums[mid] , nums[right]])
                    mid += 1
                    while mid < right and nums[mid-1] == nums[mid]: # skip duplicates
                        mid+=1
                elif temp > 0:
                    right -= 1
                else:
                    mid += 1
        return res