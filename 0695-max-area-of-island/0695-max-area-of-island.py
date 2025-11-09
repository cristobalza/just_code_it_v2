class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(r:int, c:int) -> int:

            if r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visited or grid[r][c] == 0:
                return 0
            
            visited.add((r, c))

            area = dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

            return 1 + area


        ROWS, COLS, visited = len(grid), len(grid[0]), set()

        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    res = max(res, dfs(r, c))
        return res
        