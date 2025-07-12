class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def backtrack(i, subset):

            if tuple(subset) not in res:
                res.add(tuple(subset.copy()))

            for j in range(i, len(nums)):

                subset.append(nums[j])

                backtrack(j + 1, subset)

                subset.pop()

                backtrack(j + 1, subset)

            return

        
        res = set()

        backtrack(0, list())

        return list(res)


            
        