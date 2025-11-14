class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        stack = []

        for i, intvl in enumerate(intervals):
            
            if newInterval[1] < intvl[0]:
                stack.append(newInterval)
                return stack + intervals[i:]

            if intvl[1] < newInterval[0]:
                stack.append(intvl)

            else:
                newInterval = [
                    min(newInterval[0], intvl[0]),
                    max(newInterval[1], intvl[1])
                ]
            
        stack.append(newInterval)

        return stack