class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        #. A power of 4 is also a power of 2
        # How to indetify it, if the n % 3 which is one less than 4, is 1

        return n > 0 and (n & (n - 1)) == 0 and n % 3 == 1