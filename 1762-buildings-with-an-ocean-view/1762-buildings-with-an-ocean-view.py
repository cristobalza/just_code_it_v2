class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        """

        heights = [4,2,3,1]
                         i

        stack = [0, 2, 3]

        monotonally decreasing as

        """

        stack = [] # store indexes

        for i, h in enumerate(heights):

            # pop values that are <= current h (not useful as curr h is taller than last h)
            while stack and heights[stack[-1]] <= h:
                stack.pop()

            stack.append(i)

        return stack



        