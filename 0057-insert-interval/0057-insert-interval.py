class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        stack = []

        for i, iv in enumerate(intervals):

            if newInterval[1] < iv[0]:
                stack.append(newInterval)
                return stack + intervals[i:]

            elif iv[1] < newInterval[0]:
                stack.append(iv)
            
            else:
                newInterval = [
                    min(iv[0], newInterval[0]),
                    max(iv[1], newInterval[1])
                    ]
            
        stack.append(newInterval)

        return stack