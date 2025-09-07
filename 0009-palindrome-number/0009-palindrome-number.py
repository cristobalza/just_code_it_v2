class Solution:
    def isPalindrome(self, x: int) -> bool:
        # If negative
        # Or if its a tenth number such as 20, 30, 40
        # Ends in 0 => multiple of 10 
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverse_x = 0

        while x > reverse_x: # 121 > 0; 12 > 1; 1 > 12

            reverse_x = reverse_x * 10 + (x % 10) # 10 + 2

            x = x // 10 # 1

        return x == reverse_x or x == reverse_x // 10