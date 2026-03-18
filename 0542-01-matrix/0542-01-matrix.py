class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        ROWS, COLS = len(mat), len(mat[0])

        res = [[0]* COLS for _ in range(ROWS)]

        visited = set()

        q = collections.deque()

        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    q.append((r, c, 0))
                    visited.add((r, c))


        while q:
            r, c, steps = q.popleft()

            for adj_r, adj_c in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:

                if (adj_r, adj_c) not in visited and (0 <= adj_r < ROWS and 0 <= adj_c < COLS):

                    visited.add((adj_r, adj_c))
                    q.append((adj_r, adj_c, steps + 1))

                    res[adj_r][adj_c] = steps + 1


        return res
