class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ROWS = len(text1)
        COlS = len(text2)

        dp = [[0] * (COlS + 1) for _ in range(ROWS + 1)]

        for r in range(1, ROWS + 1):
            for c in range(1, COlS + 1):
                if text1[r - 1] == text2[c - 1]:
                    dp[r][c] = 1 + dp[r - 1][c - 1]
                else:
                    dp[r][c] = max(dp[r - 1][c], dp[r][c - 1])

        return dp[-1][-1]