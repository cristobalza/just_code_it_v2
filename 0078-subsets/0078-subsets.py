class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(i, subset):

            
            if i == len(nums):
                res.add(tuple(subset[::]))
                return 

            subset.append(nums[i])

            backtrack(i+1, subset)

            subset.pop()

            backtrack(i+ 1, subset)

            return 

        res = set()
        backtrack(0, [])

        return list(res)
                