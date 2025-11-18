class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        prev = intervals[0]

        count = 0

        for i in range(1, len(intervals)):
            curr = intervals[i]

            if prev[1] > curr[0]:
                count += 1

                prev = [prev[0], min(prev[1], curr[1])]

            else:
                prev = curr

        return count
        