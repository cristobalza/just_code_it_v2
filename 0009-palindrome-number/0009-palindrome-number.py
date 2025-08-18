class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0): 
            return False

        reverse_x_int = 0

        while x > reverse_x_int:
            reverse_x_int = reverse_x_int * 10 + x % 10

            x //= 10

        return x == reverse_x_int or x == reverse_x_int // 10