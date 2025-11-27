class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(i, curr_sum, subset):

            if curr_sum == target:
                res.append(subset[::])
                return

            if curr_sum > target:
                return

            for j in range(i, len(candidates)):

                curr_sum += candidates[j]
                subset.append(candidates[j])

                backtrack(j, curr_sum, subset)

                curr_sum -= candidates[j]
                subset.pop()

            return 

        res = []
        backtrack(0, 0, [])
        return res

                
