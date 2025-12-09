class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = [] # store indexes
        next_smaller = [n] * n
        prev_smaller = [-1] * n

        for i, h in enumerate(heights):
            
            # pop values that are > h (next smaller)
            while stack and heights[stack[-1]] > h:
                stack_top = stack.pop()
                next_smaller[stack_top] = i

            if stack:
                prev_smaller[i] = stack[-1]

            stack.append(i)

        res = 0

        for i, h in enumerate(heights):
            w = next_smaller[i] - prev_smaller[i] - 1
            area = h * w
            res = max(res, area)

        return res

