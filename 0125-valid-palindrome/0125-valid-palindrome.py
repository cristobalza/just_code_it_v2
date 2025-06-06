class Solution:
    def isPalindrome(self, s: str) -> bool:
        def is_al_num(char):
            return (
                (ord("A") <= ord(char) <= ord("Z")) or
                (ord("a") <= ord(char) <= ord("z")) or
                (ord("0") <= ord(char) <= ord("9"))
            )

        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not is_al_num(s[l]):
                l += 1
            while l < r and not is_al_num(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l+= 1
            r-= 1

        return True

