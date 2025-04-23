class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        intervals.sort(key=lambda x: x[0])

        for i, curr in enumerate(intervals):
            if i == 0:
                continue
            prev = intervals[i-1]
            if prev[1] > curr[0]:
                return False
        return True