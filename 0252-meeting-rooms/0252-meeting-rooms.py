class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) == 0:
            return True
        
        intervals.sort(key=lambda x:x[0])
        prev = intervals[0]

        for i, iv in enumerate(intervals[1:]):
            if prev[1] > iv[0]:
                return False
            else:
                prev = iv

        return True
        