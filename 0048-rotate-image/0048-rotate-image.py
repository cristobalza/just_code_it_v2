class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m, n = len(matrix), len(matrix[0])

        # Transpose
        for row in range(m):
            for col in range(row, n):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        # Reflection
        for row in range(m):
            for col in range(n // 2):
                matrix[row][col], matrix[row][-col - 1] = matrix[row][-col - 1], matrix[row][col]