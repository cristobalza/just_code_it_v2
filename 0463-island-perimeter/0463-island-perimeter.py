class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()

        ROWS, COLS = len(grid), len(grid[0])

        perimeter = 0

        def dfs(r, c, visited):
            nonlocal perimeter, ROWS, COLS

            if (r, c) in visited:
                return 

            if r == ROWS or r < 0 or c == COLS or c < 0 or grid[r][c] == 0:
                perimeter += 1
                return
            
            visited.add((r, c))

            for _r, _c in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                dfs(_r, _c, visited)

            return 
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    dfs(r, c, visited)
                    
        return perimeter

            
        