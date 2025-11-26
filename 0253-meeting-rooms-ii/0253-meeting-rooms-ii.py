class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        intervals = [[0,30],[5,10],[15,20]]

        start_list [[0,30],[5,10],[15,20]]
        end_list   [[5,10],[15,20],[0,30]]

        """
        
        start_list = sorted(intervals, key=lambda x:x[0])
        end_list = sorted(intervals, key=lambda x:x[1])

        start_i, end_i = 0, 0

        rooms = 0
        max_rooms = 0

        while start_i < len(intervals):

            if start_list[start_i][0] < end_list[end_i][1]:
                start_i += 1
                rooms += 1

            else:
                end_i += 1
                rooms -= 1
            
            max_rooms = max(max_rooms, rooms)
        
        return max_rooms
