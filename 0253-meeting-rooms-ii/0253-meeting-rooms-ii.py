class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        start_list = sorted([iv[0] for iv in intervals])
        end_list = sorted([iv[1] for iv in intervals])

        res, count = 0, 0

        s, e = 0, 0

        while s < len(intervals):

            if start_list[s] < end_list[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1

            res = max(res, count)

        return res
        