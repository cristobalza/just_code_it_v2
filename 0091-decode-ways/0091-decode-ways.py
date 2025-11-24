class Solution:
    def numDecodings(self, s: str) -> int:
        # Memoization

        def dfs(i):
            # Base case
            if i == len(s):
                return 1

            if s[i] == "0":
                return 0

            if i in memo:
                return memo[i]

            memo[i] = dfs(i + 1) # Single digit decode

            # Double digit decode
            if i + 1 < len(s):
                two_digits = s[i:i + 2]
                if 10 <= int(two_digits) <= 26:
                    memo[i] += dfs(i + 2)

            return memo[i]

        memo = {}
        return dfs(0)
