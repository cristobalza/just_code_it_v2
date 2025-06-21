class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        _s = [ch if ch.isalnum() else "" for ch in s]
        _s = "".join(_s)
        l, r = 0, len(_s) - 1

        while l <= r:
            if _s[l] != _s[r]:
                return False
            l += 1
            r -= 1

        return True
