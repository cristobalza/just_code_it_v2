class Solution:
    def longestPalindrome(self, s: str) -> str:
        idx = 0
        size = 0
        n = len(s)

        for i in range(n):
            
            l, r = i, i
            while 0 <= l and r < n and s[l] == s[r]:
                if (r - l + 1) > size:
                    idx = l
                    size = r - l + 1
                
                l -= 1
                r += 1

            l, r = i, i + 1
            while 0 <= l and r < n and s[l] == s[r]:
                if (r - l + 1) > size:
                    idx = l
                    size = r - l + 1
                
                l -= 1
                r += 1
        
        return s[idx: idx + size]