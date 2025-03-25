class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        
        stack = []
        stack.append(intervals[0])

        for curr_interval in intervals[1:]:
            if stack[-1][1] >= curr_interval[0]:
                last_interval = stack.pop()
                last_interval[1] = max(curr_interval[1], last_interval[1])
                stack.append(last_interval)
            else:
                stack.append(curr_interval)
        
        return stack