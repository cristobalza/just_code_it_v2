class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = [[0]*len(matrix[0]) for _ in range(len(matrix))]

        for r in range(len(self.prefix)):
            self.prefix[r][0] = matrix[r][0]

            for c in range(1, len(self.prefix[0])):
                self.prefix[r][c] = self.prefix[r][c - 1] + matrix[r][c]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        res = 0

        for r in range(row1, row2 + 1):
            val = self.prefix[r][col2] - self.prefix[r][col1-1] if col1 > 0 else self.prefix[r][col2]
            res += val
        
        return res
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)