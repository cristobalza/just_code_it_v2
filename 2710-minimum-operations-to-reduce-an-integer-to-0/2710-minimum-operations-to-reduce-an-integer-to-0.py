class Solution:
    def minOperations(self, n: int) -> int:
        """
        Step 1: Find x st 2^x <= n < 2^(x+1) =>(log2) x <= log2(n) < x+1 ==> x = log2(n) 
        Step 2: Find n st n = min(2^x - n, 2^(x+1) - n)
        Step 3: Keep doing it until n == 0

        For n = 39

        x = log2(39) = 5
        2^5 (32) <= 39 < 2^(6) (64)
        n = min(39 - 32, 64 - 39) = 7
        res = 1

        x = log2(7) = 3
        2^3 (8) <= 7 < 2^(4) (16)
        n = min(7 - 8, 16 - 7) = 1
        res = 2

        x = log2(1) = 1
        2^1 (2) <= 1 < 2^(2) (4)
        n = 0
        res = 3

        """
        import numpy as np

        res = 0

        while n > 0:
            x = floor(np.log2(n))
            n = min(abs(2**(x) - n), 2**(x+1) - n)
            res += 1
        
        return res
