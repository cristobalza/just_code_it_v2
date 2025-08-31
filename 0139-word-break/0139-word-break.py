class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(n - 1, -1, -1):
            for word in wordDict:
                word_size = len(word)
                if i + word_size <= n and word == s[i: i + word_size]:
                    dp[i] = dp[i + word_size]
                if dp[i]:
                    break

        return dp[0]