class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        ROWS, COLS = len(matrix), len(matrix[0])

        bag = []

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    bag.append((r, c))

        for r, c in bag:
            # To right
            for _c in range(c + 1, COLS):
                matrix[r][_c] = 0

            # To left
            for _c in range(COLS - 1, -c, -1):
                matrix[r][_c] = 0

            # Up
            for _r in range(r + 1, ROWS):
                matrix[_r][c] = 0

            # Down
            for _r in range(ROWS-1, -r, -1):
                matrix[_r][c] = 0

            