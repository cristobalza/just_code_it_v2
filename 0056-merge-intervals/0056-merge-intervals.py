class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x : x[0])
        stack = []
        stack.append(intervals[0])

        for start, end in intervals[1:]:
            last_in_stack = stack[-1][1]

            if last_in_stack < start:
                stack.append([start, end])
            else:
                stack[-1][1] = max(end, stack[-1][1])

        return stack
        