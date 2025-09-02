class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(r, c):
            if validate(r, c):
                visited.add((r, c))

                for _r, _c in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    dfs(_r, _c)
            

        
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        validate = lambda r, c: 0 <= r and 0 <= c and r < ROWS and c < COLS and grid[r][c] == "1" and (r, c) not in visited

        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == "1":
                    res += 1
                    dfs(r, c)

        return res
