class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        max_len = 0

        l = 0

        n = len(s)

        for i in range(n):
            
            l, r = i, i # odd

            while 0 <= l and r < n and s[l] == s[r]:
                if (r - l + 1) > max_len:
                    max_len = r - l + 1
                    res = s[l: r + 1]

                l -= 1
                r += 1


            l, r = i, i + 1 # even

            while 0 <= l and r < n and s[l] == s[r]:
                if (r - l + 1) > max_len:
                    max_len = r - l + 1
                    res = s[l: r + 1]

                l -= 1
                r += 1

        return res