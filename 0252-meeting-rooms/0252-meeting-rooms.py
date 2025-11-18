class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) == 0:
            return True

        intervals.sort(key=lambda x: x[0])

        prev = intervals[0]

        for i in range(1, len(intervals)):
            curr = intervals[i]

            if prev[1] > curr[0]:
                return False

            prev = curr

        return True