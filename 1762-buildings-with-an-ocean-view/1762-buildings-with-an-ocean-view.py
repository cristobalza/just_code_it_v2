class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        """
        Given
            heights: array int
        
        A builiding has an ocean view, if all of the buildings right to it have smaller height

        Return
            list of indices of buildings that actually have a ocean view, sorted increasing

        Example 1:
        Input: heights = [4,2,3,1]
                                i

        [0, 2, 3]

        monotonically increasing

        """

        stack = []

        for i, h in enumerate(heights):

            while stack and heights[stack[-1]] <= h:
                stack.pop()

            stack.append(i)

        return stack
        