class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # dfs

        visited = set()
        m, n = len(grid), len(grid[0])
        perimeter = 0

        def dfs(row, col):
            nonlocal visited, m, n, perimeter

            if (row, col) not in visited and 0 <= row < m and 0 <= col < n:
                visited.add((row, col))
                # Check north
                if (row - 1 >= 0 and grid[row - 1][col] == 0) or row - 1 < 0:
                    perimeter += 1
                # Check south
                if (row + 1 < m and grid[row + 1][col] == 0) or row + 1 == m:
                    perimeter += 1
                # Check west
                if (col - 1 >= 0 and grid[row][col - 1] == 0) or col - 1 < 0:
                    perimeter += 1
                # Check east
                if (col + 1 < n and grid[row][col + 1] == 0) or col + 1 == n:
                    perimeter += 1
            
            # Explore
            explore_list = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
            for next_row, next_col in explore_list:
                if 0 <= next_row < m and 0 <= next_col < n and grid[next_row][next_col] == 1 and (next_row, next_col) not in visited:
                    dfs(next_row, next_col)
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    dfs(row, col)
        return perimeter


        