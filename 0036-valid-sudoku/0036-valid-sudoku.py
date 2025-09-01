class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])

        rows_hmap = collections.defaultdict(set) # value
        cols_hmap = collections.defaultdict(set)
        square_hmap = collections.defaultdict(set)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == ".":
                    continue
                else:

                    # check existance
                    if (
                        board[r][c] in rows_hmap[r] 
                        or board[r][c] in cols_hmap[c] 
                        or board[r][c] in square_hmap[(r//3,c//3)]
                    ):
                        return False
                    
                    # add new board value
                    rows_hmap[r].add(board[r][c])
                    cols_hmap[c].add(board[r][c])
                    square_hmap[(r//3, c//3)].add(board[r][c])

        return True