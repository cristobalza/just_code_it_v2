class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        
        def backtrack(start_idx, current_sum, path):
            # Base cases
            if current_sum == target:
                results.append(path[:])  # Make a copy
                return
            
            if current_sum > target:
                return
                
            # Try all candidates from the current index
            for i in range(start_idx, len(candidates)):
                num = candidates[i]
                path.append(num)
                # Pass current sum rather than recalculating
                # Allow reusing the same element (i, not i+1)
                backtrack(i, current_sum + num, path)
                path.pop()
        
        backtrack(0, 0, [])
        return results