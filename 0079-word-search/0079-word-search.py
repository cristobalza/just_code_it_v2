class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def backtrack(r, c, i, word, visited):
            if i == len(word):
                return True

            if r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visited or board[r][c] != word[i]:
                return False

            visited.add((r, c))

            res = (
                backtrack(r + 1, c, i + 1, word, visited) or
                backtrack(r - 1, c, i + 1, word, visited) or
                backtrack(r, c + 1, i + 1, word, visited) or
                backtrack(r, c - 1, i + 1, word, visited)
            )

            visited.remove((r, c))

            return res

        ROWS, COLS = len(board), len(board[0])

        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r, c, 0, word, set()):
                    return True
        return False
        