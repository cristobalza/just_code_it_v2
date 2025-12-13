class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        Given 
            trips - [[numpassengers, from, to]]
                ith - trip
            for i in range trips -> number of passegers that are located at from and need to be dropped off at to
            capacity - number of empty seats

        Return True if its possible to pick up and drop off all passengers for all given trips

        Input: trips = [[2,1,5],[3,3,7]], capacity = 4
                            i
        trips[i][0] - current num passengers 2 < capacity = 4
                3
            .-------.
            
            2
        .-------.

        | | | | | | |
        1   3.  5.  7

        THIS IS EVENT-BASED NOT INTERVALS!! 

        SO NEED TO CHECK IN AND THE OUTS!
        """
        events_list = []

        for num_pass, from_km, to_km in trips:
            events_list.append((from_km, num_pass))
            events_list.append((to_km, -num_pass))

        curr_cap = 0

        events_list.sort() 

        for _, num_pass in events_list:
            curr_cap += num_pass

            if curr_cap > capacity:
                return False

        return True





        