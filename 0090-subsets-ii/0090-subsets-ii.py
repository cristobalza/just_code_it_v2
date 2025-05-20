class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(i, subset):

            if tuple(subset) not in res:
                res.add(tuple(subset.copy()))
            
            if i == len(nums):
                return
                
            # use current nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            # skip current nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)
            return 


        res = set()
        nums.sort()
        backtrack(0, [])
        return list(res)