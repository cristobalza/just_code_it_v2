class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        res = 0
        hmap = {}
        l = 0
        
        for r in range(len(s)):
            # If character is already in window, shrink from left
            if s[r] in hmap and hmap[s[r]] >= l:
                l = hmap[s[r]] + 1
            
            # Update the character's position
            hmap[s[r]] = r
            
            # Update result with current window size
            res = max(res, r - l + 1)
            
        return res