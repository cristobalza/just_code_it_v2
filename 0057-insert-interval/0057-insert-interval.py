class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # case 1 you insert in between two intervals
        # case 2 you insert and merge one of them 
        # case 3 the new interval merges multiple intervals
        # case 4 the new interval is inserted at the begining or at the end

        stack = []

        for i, interval in enumerate(intervals):

            if interval[1] < newInterval[0]:
                stack.append(interval)

            elif newInterval[1] < interval[0]:
                stack.append(newInterval)
                return stack + intervals[i:]

            else:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]

        stack.append(newInterval)

        return stack