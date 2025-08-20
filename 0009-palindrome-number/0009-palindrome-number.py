class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        if num < 0 or (num % 10 == 0 and num != 0):
            return False
        
        reverse_num = 0

        while num > reverse_num:
            reverse_num = reverse_num * 10 + num % 10

            num = num // 10

        return num == reverse_num or num == reverse_num // 10
        