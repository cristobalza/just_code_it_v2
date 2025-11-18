class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        hmap = collections.defaultdict(int) # ch: idx
        l = 0

        for r in range(len(s)):

            if s[r] in hmap:
                l = max(l, 1 + hmap[s[r]])

            hmap[s[r]] = r

            res = max(res, r - l + 1)

        return res