class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """

        s = "AABABBA", k = 1
                  r
               l

        lenght of word - max count <= k
        
        5             -  3      ==> 2 <= 1 

        hmap = {A: 2, B: 3}




        """

        if len(s) == 0:
            return 0

        res = 1
        l = 0
        hmap = collections.defaultdict(int)

        for r in range(len(s)):

            hmap[s[r]] = hmap.get(s[r], 0) + 1

            lenght_word = r - l + 1
            max_count = max(hmap.values())

            if lenght_word - max_count > k:
                hmap[s[l]] = hmap.get(s[l]) - 1
                l += 1

            res = max(res, r - l + 1)

        return res