class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        top, bottom = 0, m - 1

        while top <= bottom:
            row = (top + bottom) // 2

            if target < matrix[row][0]:
                bottom = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                break

        l, r = 0, n - 1
        row = (top + bottom) // 2

        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] > target:
                r -= 1
            elif matrix[row][mid] < target:
                l += 1
            else:
                return True

        return False

        