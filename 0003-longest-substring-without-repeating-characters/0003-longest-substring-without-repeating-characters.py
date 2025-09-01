class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Input: s = "abcabcbb"
                     l
                       r 

     {b, c, a}

     res = 3

        """

        l = 0
        hmap = {} # ch: idx
        res = 0

        for r in range(len(s)):
            if s[r] in hmap:
                l = max(l, 1 + hmap[s[r]])
            
            hmap[s[r]] = r

            res = max(res, r - l + 1)

        return res

        