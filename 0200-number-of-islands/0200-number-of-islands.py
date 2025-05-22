class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(r, c):
            nonlocal visited

            if r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visited or grid[r][c] == "0":
                return

            visited.add((r, c))

            for _r, _c in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                dfs(_r, _c)
            
            return 

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        count = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    count += 1
                    dfs(r, c)
        return count
        



         
        
        