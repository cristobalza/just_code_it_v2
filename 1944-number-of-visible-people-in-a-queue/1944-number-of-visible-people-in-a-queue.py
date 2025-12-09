class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        """
        for every person we decide only to things.
        1. The next person with greater or equal height (no person after this would be visible to the current person). But multiple people behind the current person with bigger height can see the current person. Let's take care of them in the second point.
        2. The previous person with strictly greater height than the current person.
1 and 2 both select mutually exclusive people. Every time we find a person from both the cases, we increase their corresponding number of visisble people by 1.



        """
        # monotonically decreasing (next greatest)

        next_greater_stack = [] # store indexes 
        res = [0] * len(heights)

        for i, h in enumerate(heights):
            # pop elements that <= h 
            while next_greater_stack and heights[next_greater_stack[-1]] <= h:
                stack_top = next_greater_stack.pop()

                res[stack_top] += 1

            if next_greater_stack:
                res[next_greater_stack[-1]] += 1

            next_greater_stack.append(i)

        return res

            


        