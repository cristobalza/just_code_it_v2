class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """  

             01234567
        s = "abcabcbb"
              l
                r

        {
            a: 0
            b: 1
            c: 2
        }

        3 >= 0

        res = 1

        """

        if len(s) == 0:
            return 0

        res = 1
        l = 0
        hmap = {}

        for r in range(len(s)):

            if s[r] in hmap and hmap[s[r]] >= l:
                l = hmap[s[r]] + 1

            hmap[s[r]] = r

            res = max(res, r - l + 1)

        return res