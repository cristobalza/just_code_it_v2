class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(r, c, visited):
            if check_lambda(r, c):
                return 
            
            visited.add((r, c))

            for _r, _c in [(r + 1, c), (r, c + 1), (r, c - 1), (r - 1, c)]:
                if not check_lambda(_r, _c):
                    dfs(_r, _c, visited)

            return 


        res = 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        check_lambda = lambda r, c: r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or grid[r][c] == "0"

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == "1":
                    res += 1
                    dfs(r, c, visited)

        return res
