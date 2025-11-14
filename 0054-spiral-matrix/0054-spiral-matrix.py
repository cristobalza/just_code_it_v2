class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        E_ROWS, E_COLS = len(matrix), len(matrix[0]) 
        area = E_ROWS * E_COLS
        S_ROWS, S_COLS = 0, 0
        res = []

        i = 0

        while i < area:
            for c in range(S_COLS, E_COLS):
                res.append(matrix[S_ROWS][c])
                i += 1

            if i == area:
                break

            S_ROWS += 1

            for r in range(S_ROWS, E_ROWS):
                res.append(matrix[r][E_COLS - 1])
                i += 1

            if i == area:
                break

            E_COLS -= 1

            for c in range(E_COLS - 1, S_COLS - 1, -1):
                res.append(matrix[E_ROWS - 1][c])
                i += 1

            if i == area:
                break

            E_ROWS -= 1

            for r in range(E_ROWS - 1, S_ROWS - 1, -1):
                res.append(matrix[r][S_COLS])
                i += 1

            if i == area:
                break
            S_COLS += 1

        return res
