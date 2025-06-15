class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        max_freq = 0
        
        for r in range(len(s)):
            # Add current character to window
            count[s[r]] = count.get(s[r], 0) + 1
            
            # Update max frequency in current window
            max_freq = max(max_freq, count[s[r]])
            
            # If window is invalid (need more than k replacements)
            window_size = r - l + 1
            if window_size - max_freq > k:
                # Shrink window from left
                count[s[l]] -= 1
                l += 1
            
            # Update result
            res = max(res, r - l + 1)
            
        return res