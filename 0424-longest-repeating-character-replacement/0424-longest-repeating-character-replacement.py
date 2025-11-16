class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hmap = {}
        l = 0
        res = 0
        max_count = 0

        for r in range(len(s)):
            hmap[s[r]] = 1 + hmap.get(s[r], 0)

            max_count = max(max_count, hmap[s[r]])

            if (r - l + 1) - max_count > k:
                hmap[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
