class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        hs = set()
        m, n = len(matrix), len(matrix[0])

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    hs.add((row, col))
        
        if len(hs) == 0:
            return None
        
        def helper(target_row, target_col):
            
            # Set all rows to zero.
            for row in range(m):
                matrix[row][target_col] = 0
        
            # Set all cols to zero.
            for col in range(n):
                matrix[target_row][col] = 0

        for row, col in hs:
            helper(row, col)
        