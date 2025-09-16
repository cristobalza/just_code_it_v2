class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        """
        Input: mat = [
               0 1 2
           0  [1,2,3],
           1  [4,5,6],
           2  [7,8,9]
           3  [7,8,9]
           4  [7,8,9]


            ]

            r // 2 = 1 // 2 = 0

            diagonal down -> mat[r - 1][c - 1]

            diagonal up -> mat[r + 1][c + 1]

            depth = 0

            mat[1, ]



        """

        ROWS, COLS = len(mat), len(mat[0])
        res = []
        r, c = 0, 0

        is_going_up = True

        for _ in range(ROWS * COLS):

            res.append(mat[r][c])

            if is_going_up:
                if c == COLS - 1:
                    r += 1
                    is_going_up = False

                elif r == 0:
                    c += 1
                    is_going_up = False

                else:
                    r -= 1
                    c += 1

            else:
                if r == ROWS - 1:
                    c += 1
                    is_going_up = True

                elif c == 0:
                    r += 1
                    is_going_up = True
                else:
                    r += 1
                    c -= 1

        return res

        