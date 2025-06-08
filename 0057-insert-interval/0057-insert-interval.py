class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # case 1 you insert the newInterval and append the rest of the intervals
        # case 2 


        stack = []

        for i, interval in enumerate(intervals):

            if newInterval[1] < interval[0]:
                stack.append(newInterval)
                return stack + intervals[i:]

            elif interval[1] < newInterval[0]:
                stack.append(interval)

            else:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]

        stack.append(newInterval)

        return stack
