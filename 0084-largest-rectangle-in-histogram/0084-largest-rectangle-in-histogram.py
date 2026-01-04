class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """

        heights = [2,1,5,6,2,3]
                   i

        get next smaller and prev smaller


        """
        n = len(heights)
        next_smaller = [n] * n
        prev_smaller = [-1] * n
        stack = []

        for i, h in enumerate(heights):
            
            while stack and heights[stack[-1]] > h:
                stack_top_idx = stack.pop()
                next_smaller[stack_top_idx] = i

            if stack:
                prev_smaller[i] = stack[-1]

            stack.append(i)

        res = 0
        for i, h in enumerate(heights):
            w = next_smaller[i] - prev_smaller[i] - 1
            area = w * h
            res = max(res, area)

        return res
        

        