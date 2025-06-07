class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x : x[0])

        stack = []

        for i, interval in enumerate(intervals):
            if i == 0:
                stack.append(interval)
            if stack[-1][1] < interval[0]:
                stack.append(interval)
            else:
                start, end = stack.pop()
                stack.append([start, max(end, interval[-1])])
        
        return stack
        