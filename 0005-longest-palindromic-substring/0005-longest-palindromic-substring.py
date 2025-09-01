class Solution:
    def longestPalindrome(self, s: str) -> str:

        """
         s = "babad"
                i
               l
                 r

                l
                r
                
        """

        res = ""
        res_lenght = 0

        for i in range(len(s)):
            l, r = i, i
            while 0 <= l and r < len(s) and s[l] == s[r]:
                if res_lenght < (r - l + 1):
                    res_lenght = r - l + 1
                    res = s[l: r + 1]
                l -= 1
                r += 1

            l, r = i, i + 1
            while 0 <= l and r < len(s) and s[l] == s[r]:
                if res_lenght < (r - l + 1):
                    res_lenght = r - l + 1
                    res = s[l: r + 1]
                l -= 1
                r += 1

        return res
        