class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def backtrack(i):
            nonlocal solved

            # Base case: empty_cells_tuple_list have been reached
            if i == len(empty_cells_tuple_list):
                solved = True
                return 

            list_r, list_c = empty_cells_tuple_list[i]

            for num in range(0, 9):

                if (
                    rows_used[num][list_r] is False
                    and cols_used[num][list_c] is False
                    and block_used[list_r // 3][list_c // 3][num] is False
                    ):

                    # Mark candidate
                    rows_used[num][list_r] = True
                    cols_used[num][list_c] = True
                    block_used[list_r // 3][list_c // 3][num] = True

                    prev_val = board[list_r][list_c]
                    board[list_r][list_c] = str(num + 1)

                    # Explore further
                    backtrack(i + 1)


                    if solved:
                        return 

                    # Remove Candidates
                    rows_used[num][list_r] = False
                    cols_used[num][list_c] = False
                    block_used[list_r // 3][list_c // 3][num] = False

                    board[list_r][list_c] = prev_val

        
        rows_used = [[False] * 9 for _ in range(9)]
        cols_used = [[False] * 9 for _ in range(9)]
        block_used = [[[False] * 9 for _ in range(9)] for _ in range(9)]

        empty_cells_tuple_list = []

        for r in range(9):
            for c in range(9):
                
                if board[r][c] == ".":
                    empty_cells_tuple_list.append((r, c))

                else:
                    num_str = board[r][c]
                    num_int_idx = int(num_str) - 1
                    rows_used[num_int_idx][r] = True
                    cols_used[num_int_idx][c] = True
                    block_used[r // 3][c // 3][num_int_idx] = True

        solved = False
        backtrack(0)
        return solved
