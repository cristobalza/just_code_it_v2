class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """

        Input: s = "ABAB", k = 2
                    l
                      r 

        {
            A: 2
            B: 1
        }
        total - max_f > k
            hmap[k] -= 1
            l += 1

        3 - 2 > k
        """

        l = 0
        hmap = {}
        max_freq = 0
        res = 0

        for r in range(len(s)):
            
            hmap[s[r]] = 1 + hmap.get(s[r], 0)

            max_freq = max(max_freq, hmap[s[r]])

            if (r - l + 1) - max_freq > k:
                hmap[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)

        return res

        