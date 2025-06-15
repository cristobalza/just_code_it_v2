class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        res = 0
        hmap = collections.defaultdict(int)
        l = 0
        
        for r in range(len(s)):

            if s[r] in hmap and hmap.get(s[r], 0) >= l:
                l = hmap[s[r]] + 1
            

            hmap[s[r]] = r
            
            res = max(res, r - l + 1)
            
        return res