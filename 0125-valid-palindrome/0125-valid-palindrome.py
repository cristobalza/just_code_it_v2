class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join([ch if ch.isalnum() else "" for ch in s])

        print(s )
        
        l, r = 0, len(s) - 1

        while l < r: 
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True
        