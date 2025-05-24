class Solution:
    def fib(self, n: int) -> int:
        
        def _fib(n):
            if n <= 1:
                return n

            return _fib(n - 1) + _fib(n - 2)

        return _fib(n)