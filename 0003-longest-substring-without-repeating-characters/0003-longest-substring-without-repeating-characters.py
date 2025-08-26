class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        l = 0
        res = 1
        hmap = {}

        for r in range(len(s)):
            if s[r] in hmap:
                l = max(l, hmap[s[r]] + 1) # position after the duplicate index is located

            hmap[s[r]] = r

            res = max(res, r - l + 1)

        return res

        