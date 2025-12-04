class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 1. binary search on ROWS -> log(ROWS) == log(m)
        # 2. binary search on COLS -> log(COLS) == log(n)
        # ==> log(m) + log(n) = log(m*n)
        # space: O(1)

        ROWS, COLS = len(matrix), len(matrix[0])
        # 1. binary search on ROWS
        u, d = 0, ROWS - 1

        while u < d:
            m = (u + d) // 2

            if matrix[m][COLS - 1] == target:
                return True
            elif matrix[m][COLS - 1] < target:
                u = m + 1
            else:
                d = m

        row_pivot = u
        arr = matrix[row_pivot]
        
        # 2. binary search on COLS
        l, r = 0, COLS - 1

        while l < r:
            m = (l + r) // 2
            if arr[m] == target:
                return True
            elif arr[m] < target:
                l = m + 1
            else:
                r = m

        return True if arr[l] == target else False