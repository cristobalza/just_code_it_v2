class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        res = 0
        prev = intervals[0]

        for i, iv in enumerate(intervals[1:]):
            if prev[1] > iv[0]:
                res += 1
                prev = [iv[0], min(prev[1], iv[1])]
            else:
                prev = iv

        return res
        