class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        # Count servers in each row and column
        row_count = [0] * ROWS
        col_count = [0] * COLS
        
        # First pass: count servers in each row and column
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    row_count[r] += 1
                    col_count[c] += 1
        
        # Second pass: count servers that can communicate
        result = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    # A server can communicate if there's at least one other server
                    # in the same row OR the same column
                    if row_count[r] > 1 or col_count[c] > 1:
                        result += 1
        
        return result