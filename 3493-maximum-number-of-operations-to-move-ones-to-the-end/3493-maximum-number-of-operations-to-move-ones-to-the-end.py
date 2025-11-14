class Solution:
    def maxOperations(self, s: str) -> int:
        ones, res = 0, 0

        for i in range(len(s)):
            if s[i] == "1":
                ones += 1

            elif s[i - 1] == "1":
                res += ones

        return res