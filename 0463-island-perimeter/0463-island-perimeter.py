class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        res = 0

        visited = set()

        def dfs(r, c):
            nonlocal m, n, res, visited

            if (r, c) in visited:
                return

            if r < 0 or r == m or c < 0 or c == n or (0 <= r < m and grid[r][c] == 0) or (0 <= c < c and grid[r][c] == 0):
                res += 1
                return 

            visited.add((r, c))
            
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

            return 

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    dfs(r, c)
        return res
        