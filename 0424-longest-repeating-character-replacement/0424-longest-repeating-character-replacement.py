class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        hmap = {}
        max_freq = 0

        for r in range(len(s)):
            hmap[s[r]] = hmap.get(s[r], 0) + 1

            window_size = r - l + 1

            max_freq = max(max_freq, hmap[s[r]])

            if window_size - max_freq > k:
                hmap[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res

