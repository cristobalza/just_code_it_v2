class Solution:
    def isHappy(self, n: int) -> bool:
        
        def helper(n):
            if n == 1:
                return True

            if n in hset:
                return False

            hset.add(n)
            curr_n = 0

            while n > 0:
                curr_n = curr_n + ((n % 10)**2)

                n = n // 10

            return helper(curr_n)

        hset = set()
        return helper(n)