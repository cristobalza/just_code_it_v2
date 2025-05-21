class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = collections.defaultdict(int)
        res = 0
        l = 0

        for r in range(len(s)):

            hm[s[r]] += 1

            # check current window is valid
            # current lenght - max frequency in the hm = times to swap
            while (r - l + 1) - max(hm.values()) > k:
                hm[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res

