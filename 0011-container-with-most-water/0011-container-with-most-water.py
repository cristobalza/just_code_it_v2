class Solution:
    def maxArea(self, height: List[int]) -> int:
        # sliding window O(N) time and O(1) space

        l = 0
        r = len(height) - 1
        res = 0

        while l < r:

            area = min(height[l], height[r]) * (r - l)

            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                

        
        return res
