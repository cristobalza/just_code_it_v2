class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(i, subset, _sum):
            
            if _sum == target:
                res.append(subset.copy())
                return

            if _sum > target or i == len(candidates):
                return

            # use current candidates[i]
            subset.append(candidates[i])
            backtrack(i + 1, subset, _sum + candidates[i])
            subset.pop()

            # skip current candidates[i]
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, subset, _sum)

            return 

        res = []
        candidates.sort()
        backtrack(0, [], 0)
        return res
