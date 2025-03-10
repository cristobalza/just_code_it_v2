class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check no dups in given row
        # Check no dups in given col
        # Check no dups in given square -> check r//3, c//3

        row_dict = collections.defaultdict(set)
        col_dict = collections.defaultdict(set)
        square_dict = collections.defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if (
                    board[row][col] in row_dict[row] or
                    board[row][col] in col_dict[col] or
                    board[row][col] in square_dict[(row // 3, col // 3)]
                ):
                    return False
                else:
                    row_dict[row].add(board[row][col])
                    col_dict[col].add(board[row][col])
                    square_dict[(row // 3, col // 3)].add(board[row][col])
        return True