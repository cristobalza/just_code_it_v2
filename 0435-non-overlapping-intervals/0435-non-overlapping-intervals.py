class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort it 
        # iterate through and check for start and end 
            # use a stack store only the non overlapping ones
        # substract the len(stack) - len(intervals)

        intervals.sort(key=lambda x: x[0])

        stack = []

        for i, interval in enumerate(intervals):

            if i == 0:
                stack.append(interval)

            elif interval[1] < stack[-1][1]:
                stack.pop()
                stack.append(interval)
            elif stack[-1][1] > interval[0]:
                continue
            else:
                stack.append(interval)

        return len(intervals) - len(stack)
        