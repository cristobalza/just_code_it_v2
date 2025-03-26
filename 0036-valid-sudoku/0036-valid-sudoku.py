class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        m, n = len(board), len(board[0])

        row_dict = collections.defaultdict(set)
        col_dict = collections.defaultdict(set)
        square_dict = collections.defaultdict(set)

        for r in range(m):
            for c in range(n):
                current_entry = board[r][c]
                if current_entry == ".":
                    continue

                if (
                    current_entry in row_dict[r] or
                    current_entry in col_dict[c] or 
                    current_entry in square_dict[(r // 3, c // 3)]
                    ):
                    return False
                else:
                    row_dict[r].add(current_entry)
                    col_dict[c].add(current_entry)
                    square_dict[(r // 3, c // 3)].add(current_entry)

        return True

