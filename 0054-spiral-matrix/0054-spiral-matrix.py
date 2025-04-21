class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        m, n = len(matrix), len(matrix[0])

        area = m * n

        upper_limit, bottom_limit, left_limit, right_limit = 0, m, 0, n

        res = []

        while area > 0: 

            # To Right
            for col in range(left_limit, right_limit):
                area -= 1
                res.append(matrix[upper_limit][col])
            upper_limit += 1
            if area == 0:
                break

            # To Down
            for row in range(upper_limit, bottom_limit):
                area -= 1
                res.append(matrix[row][right_limit - 1])
            right_limit -= 1
            if area == 0:
                break

            # To Left
            for col in range(right_limit - 1, left_limit - 1 , -1):
                area -= 1
                res.append(matrix[bottom_limit - 1][col])
            bottom_limit -= 1
            if area == 0:
                break

            # To Up
            for row in range(bottom_limit - 1, upper_limit - 1, -1):
                area -= 1
                res.append(matrix[row][left_limit])
            left_limit += 1
        
        return res
