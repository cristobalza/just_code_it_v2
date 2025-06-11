class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        """

            ---
          ---
        -----
        ---
        1 2 3 4
        """

        res = 0

        intervals.sort(key=lambda x: x[0])

        prev = intervals[0]

        for i, iv in enumerate(intervals[1:]):

            if prev[1] > iv[0]:
                res += 1
                prev = [iv[0], min(iv[1], prev[1])]

            else:
                prev = iv
                
        return res
        



        