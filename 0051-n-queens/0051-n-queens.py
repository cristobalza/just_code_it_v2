class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col_set = set()
        positive_diag_set = set()
        negative_diag_set = set()

        board = [
            ["."] * n for _ in range(n)
        ]

        res = []

        def backtrack(r):

            if r == n:
                res.append(["".join(board[row]) for row in range(n)])
                return
            else:
                for c in range(n):
                    if c not in col_set and r + c not in positive_diag_set and r - c not in negative_diag_set:
                        board[r][c] = "Q"
                        col_set.add(c)
                        positive_diag_set.add(r + c)
                        negative_diag_set.add(r - c)

                        backtrack(r + 1)

                        board[r][c] = "."
                        col_set.remove(c)
                        positive_diag_set.remove(r + c)
                        negative_diag_set.remove(r - c)

        backtrack(0)
        return res