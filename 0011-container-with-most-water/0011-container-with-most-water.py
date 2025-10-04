class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1

        res = 0

        while l < r:
            width = r - l 
            min_height = min(height[l], height[r])

            res = max(res, width * min_height)

            if height[l] < height[r]:
                l += 1

            else:
                r -= 1

        return res

        