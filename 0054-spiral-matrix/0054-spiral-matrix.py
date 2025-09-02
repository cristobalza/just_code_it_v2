class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])

        limit_top = 0
        limit_bottom = 0
        limit_left = 0
        limit_right = 0

        res = []

        i = 0
        size = ROWS * COLS

        while i < size:

            # Right traversal
            for c in range(limit_left, COLS - limit_right):
                if i == size:
                    break
                i += 1
                res.append(matrix[limit_top][c])

            limit_top += 1

            # Down traversal
            for r in range(limit_top, ROWS - limit_bottom):
                if i == size:
                    break
                i += 1
                res.append(matrix[r][COLS - 1 - limit_right])
            
            limit_right += 1

            # Left traversal
            for c in range(COLS - 1 - limit_right, limit_left - 1, -1):
                if i == size:
                    break
                i += 1
                res.append(matrix[ROWS - 1 - limit_bottom][c])
            
            limit_bottom += 1

            # Up traversal
            for r in range(ROWS - 1 - limit_top, limit_bottom - 1, -1):
                if i == size:
                    break
                i += 1
                res.append(matrix[r][limit_left])

            limit_left += 1
        
        return res

