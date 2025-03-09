class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def dfs(row, col, ocean_set, prev_height):
            nonlocal m, n, heights

            if 0 <= row < m and 0 <= col < n and (row, col) not in ocean_set and heights[row][col] >= prev_height:
                ocean_set.add((row, col))
            
                for next_row, next_col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                    dfs(next_row, next_col, ocean_set, heights[row][col])
        

        m, n = len(heights), len(heights[0])

        pacific_set, atlantic_set = set(), set()

        for row in range(m):
            dfs(row, 0, pacific_set, heights[row][0])
            dfs(row, n - 1, atlantic_set, heights[row][n - 1])

        for col in range(n):
            dfs(0, col, pacific_set, heights[0][col])
            dfs(m - 1, col, atlantic_set, heights[m - 1][col])


        res = []
        for row in range(m):
            for col in range(n):
                if (row, col) in pacific_set and (row, col) in atlantic_set:
                    res.append([row, col])

        return res 