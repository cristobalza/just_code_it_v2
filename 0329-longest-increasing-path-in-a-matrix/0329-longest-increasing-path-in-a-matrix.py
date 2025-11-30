class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        def dfs(r, c, prev_val):
            if min(r, c) < 0 or r == ROWS or c == COLS or matrix[r][c] <= prev_val: 
                return 0

            if (r, c) in memo:
                return memo[(r, c)]

            memo[(r, c)] = 1

            for _r, _c in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                curr_val = matrix[r][c]
                memo[(r, c)] = max(memo[(r, c)], 1 + dfs(_r, _c, curr_val))

            return memo[(r, c)]
        
        res = 0
        ROWS, COLS = len(matrix), len(matrix[0])
        memo = {}

        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c, float("-inf")))

        return res