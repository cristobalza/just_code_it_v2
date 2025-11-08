class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def backtrack(r, c, i):

            if i == len(word):
                return True

            if 0 <= r < ROWS and 0 <= c < COLS and i < len(word) and (r, c) not in visited and board[r][c] == word[i]:
                visited.add((r, c))
                for _r, _c in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if backtrack(_r, _c, i + 1):
                        return True
                visited.remove((r, c))

            return False

        visited, ROWS, COLS = set(), len(board), len(board[0])

        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r, c, 0):
                    return True

        return False