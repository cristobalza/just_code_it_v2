class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def dfs(x, n):
            if x == 1 or n == 0:
                return 1

            if x == 0:
                return 0

            if x in memo:
                return memo[x]

            if n % 2 == 0:
                memo[x] = dfs(x * x, n //2)
            else:
                memo[x] = dfs(x, n - 1) * x

            return memo[x]
        
        memo = {}
        res = dfs(x, abs(n))
        return res if n > 0 else 1/res
