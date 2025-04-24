class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        res = 1

        for i in range(len(s)):
            hs = set()
            hs.add(s[i])
            for j in range(i+1, len(s)):
                if s[j] in hs:
                    break
                else:
                    hs.add(s[j])
            res = max(res, len(hs))
        return res