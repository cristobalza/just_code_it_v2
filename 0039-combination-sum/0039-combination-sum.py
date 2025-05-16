class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(i, subset):

            if subset and sum(subset) == target:
                res.add(tuple(subset[:]))
                return 

            if subset and sum(subset) > target:
                return

            for j in range(i, len(candidates)):
                subset.append(candidates[i])
                backtrack(j, subset)
                subset.pop()
            
            return 

        res = set()

        for i in range(len(candidates)):
            backtrack(i, [])

        return list(res)
        