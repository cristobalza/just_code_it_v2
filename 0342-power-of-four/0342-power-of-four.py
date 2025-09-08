class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        if n < 0:
            return False

        x = 1

        while x <= n: # 4^k <= n => log4(n) >= k
        # Therefore, the number of iterations is proportional to log4(n), giving us O(log4(n)) time complexity.
            if x == n:
                return True

            x *= 4

        return False