class Solution:
    def numberOfMatches(self, n: int) -> int:
        res = 0
        while n > 1:
            if n % 2 == 0:
                res += n // 2 # matches played
                n = n // 2 # team advanced
            else:
                res += (n - 1) // 2 # matches played
                n = (n - 1) // 2 + 1 # team advanced
        return res
        