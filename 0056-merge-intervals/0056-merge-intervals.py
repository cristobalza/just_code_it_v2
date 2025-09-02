class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        stack = []
        stack.append(intervals[0])

        for i in range(1, len(intervals)):
            prev_interval = stack[-1]
            curr_interval = intervals[i]

            if prev_interval[1] >= curr_interval[0]:
                new_interval = [min(prev_interval[0], curr_interval[0]), max(prev_interval[1], curr_interval[1])]
                stack.pop()
                stack.append(new_interval)
            else:
                stack.append(curr_interval)

        return stack
