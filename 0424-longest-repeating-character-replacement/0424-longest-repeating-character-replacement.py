class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Input: s = "ABAB", k = 2 ; k=0
                    l
                       r
                r - l + 1
                s[l] != s[r] -> what's the count of s[l]?

                s[l] = 2, k = 2 , totla = r - l + 1 = 3 - 0 + 1 = 4

                4 - 2 <= k = 2

        {
            A: 2
            B: 2
        }
        sliding window approach

        """

        l = 0
        res = 0
        hmap = collections.defaultdict(int) # char: frequency
        max_frequency = 0 # number of characters we don't want to repleace

        for r in range(len(s)):

            hmap[s[r]] = hmap.get(s[r], 0) + 1

            size_substring = r - l + 1

            max_frequency = max(max_frequency, hmap[s[r]])

            if size_substring - max_frequency > k:
                hmap[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)

        return res
