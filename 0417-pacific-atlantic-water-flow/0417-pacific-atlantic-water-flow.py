class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Run dfs from atlantic (ROWS, 0) to pacific (0, COLS)

        def dfs(r, c, visited, prev_h):
            
            if (r, c) in visited or r < 0 or c < 0 or r == ROWS or c == COLS:
                return 

            curr_h = heights[r][c]

            if prev_h > curr_h:
                return
            
            visited.add((r, c))
        
            for _r, _c in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                dfs(_r, _c, visited, curr_h)
            
            return

        
        ROWS, COLS = len(heights), len(heights[0])

        atlantic_set, pacific_set = set(), set()

        for r in range(ROWS):
            dfs(r, 0, pacific_set, heights[r][0])
            dfs(r, COLS - 1, atlantic_set, heights[r][COLS - 1])

        for c in range(COLS):
            dfs(0, c, pacific_set, heights[0][c])
            dfs(ROWS - 1, c, atlantic_set, heights[ROWS - 1][c])

        res = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific_set and (r, c) in atlantic_set:
                    res.append((r, c))

        return res
