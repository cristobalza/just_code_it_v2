class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def dfs(r, c, prev_h, visited):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited:
                return
            
            curr_h = heights[r][c]

            if curr_h < prev_h:
                return 

            visited.add((r, c))

            for _r, _c in [(r+1, c),(r-1, c),(r, c+1),(r, c-1)]:
                dfs(_r, _c, curr_h, visited)
            
            return 

        ROWS, COLS = len(heights), len(heights[0])
        pacific_set, atlantic_set = set(), set()

        res = []

        for c in range(COLS):
            dfs(0, c, float("-inf"), pacific_set)
            dfs(ROWS - 1, c, float("-inf"), atlantic_set)

        for r in range(ROWS):
            dfs(r, 0, float("-inf"), pacific_set)
            dfs(r, COLS - 1, float("-inf"), atlantic_set)

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific_set and (r, c) in atlantic_set:
                    res.append((r, c))

        return res