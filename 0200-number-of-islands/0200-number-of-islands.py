class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(r, c):
            if  0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == "1":
                grid[r][c] = "0"

                for _r, _c in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    dfs(_r, _c)

        
        ROWS, COLS = len(grid), len(grid[0])
        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    res += 1
                    dfs(r, c)

        return res
                