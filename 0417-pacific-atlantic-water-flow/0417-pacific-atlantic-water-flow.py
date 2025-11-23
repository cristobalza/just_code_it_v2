class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def dfs(r, c, prev_height, visited):
            if 0 <= r < ROWS and 0 <= c < COLS and (r, c) not in visited and heights[r][c] >= prev_height:
                visited.add((r, c))

                for _r, _c in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    dfs(r + _r, c + _c, heights[r][c], visited)
            return

        ROWS, COLS = len(heights), len(heights[0])

        pacific_set, atlantic_set = set(), set()

        for r in range(ROWS):
            dfs(r, 0, float("-inf"), pacific_set)
            dfs(r, COLS-1, float("-inf"), atlantic_set)

        for c in range(COLS):
            dfs(0, c, float('-inf'), pacific_set)
            dfs(ROWS-1, c, float("-inf"), atlantic_set)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific_set and (r, c) in atlantic_set:
                    res.append((r, c))
        return res