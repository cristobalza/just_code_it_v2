class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        s = "AABABBA", k = 1
                   r
                l

        hmap {
            A: 2
            B: 2

        }
        max_freq = 3

        (r - l + 1) - max_freq > k
        4 - 3 > 1
            hmap[s[l]] -= 1
            l += 1


        res = 4



        """
        hmap = {} # store char: count
        res = 0
        l = 0
        max_freq = 0

        for r in range(len(s)):
            hmap[s[r]] = hmap.get(s[r], 0) + 1

            max_freq = max(max_freq, hmap[s[r]])

            while (r - l + 1) - max_freq > k:
                hmap[s[l]] -= 1
                l += 1
                
            res = max(res, r - l + 1)

        return res
