class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m, n = len(matrix), len(matrix[0])
        zeroes_hs = set()
        
        # Collect zeroes
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    zeroes_hs.add((r, c))

        
        # Explore
        while zeroes_hs:
            pivot_r, pivot_c = zeroes_hs.pop()

            # Go down
            for r in range(pivot_r + 1, m):
                matrix[r][pivot_c] = 0

            # Go up
            for r in range(m - 1, -pivot_r - 1, -1):
                matrix[r][pivot_c] = 0

            # Go right
            for c in range(pivot_c + 1, n):
                matrix[pivot_r][c] = 0

            # Go left
            for c in range(n - 1, -pivot_c - 1, -1):
                matrix[pivot_r][c] = 0
