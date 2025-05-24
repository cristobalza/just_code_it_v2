class Solution:
    def fib(self, n: int) -> int:
        
        def _fib(n, memo):
            if n <= 1:
                return n

            if n in memo:
                return memo[n]
            
            memo[n] = _fib(n - 1, memo) + _fib(n - 2, memo)
            
            return memo[n]

        return _fib(n, {})