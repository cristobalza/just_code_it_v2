class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_hl, max_hr = height[l], height[r]
        res = 0

        while l < r:
            if max_hl < max_hr:
                l += 1
                max_hl = max(max_hl, height[l])
                res += (max_hl - height[l])
            else:
                r -= 1
                max_hr = max(max_hr, height[r])
                res += (max_hr - height[r])
        
        return res