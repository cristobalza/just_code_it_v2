class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l, r = 0, 0
        hs = set()

        while r < len(s):

            while s[r] in hs:
                hs.remove(s[l])
                l += 1
                
            hs.add(s[r])
            res = max(res, r - l + 1)
            r += 1

        return res