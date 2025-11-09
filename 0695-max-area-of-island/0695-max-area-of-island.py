class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(r:int, c:int) -> int:

            if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            
            area = dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

            return 1 + area


        ROWS, COLS = len(grid), len(grid[0])

        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))
        return res
        