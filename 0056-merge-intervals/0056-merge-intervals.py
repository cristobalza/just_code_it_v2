class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        stack = []
        stack.append(intervals[0])

        for i in range(1, len(intervals)):
            curr = intervals[i]

            if stack[-1][1] >= curr[0]:
                prev = stack.pop()
                new_intv = [
                    min(prev[0], curr[0]),
                    max(prev[1], curr[1])
                ]
                stack.append(new_intv)

            else:
                stack.append(curr)

        return stack
