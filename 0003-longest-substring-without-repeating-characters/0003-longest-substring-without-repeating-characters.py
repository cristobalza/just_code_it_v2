class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        s = "abcabcbb"
                l
                 r

        {
            a: 0 + 3 = 3
            b: 1 + 
            c: 2
        }

        res = 3


        """
        hmap = collections.defaultdict(int) # letter: count

        l = 0

        res = 0
        
        for r in range(len(s)):
            if s[r] in hmap:
                l = max(l, 1 + hmap[s[r]])

            hmap[s[r]] = r

            res = max(res, r - l + 1)

        return res