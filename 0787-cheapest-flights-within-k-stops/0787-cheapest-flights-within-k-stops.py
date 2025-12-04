class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        Djikstra to find "shortest path" as a cheapest path to destination

        Given
            n - cities
            flights - flights[i] = [from, to, price]

            src -> init
            dst -> goal!
            k -> number of stops

            For those unreacheable nodes -> -1

        """

        adj = collections.defaultdict(list) # src: [(destination, price)]

        for src_city, destination_city, price in flights:
            adj[src_city].append((destination_city, price))

        minheap = [] # (price, src, stops)
        minheap.append((0, src, 0))

        shortest = {} # (city, stops): price

        while minheap:
            price, city, stops = heapq.heappop(minheap)
            
            if city == dst:
                return price

            if stops > k:
                continue

            if (city, stops) in shortest and shortest[(city, stops)] <= price:
                continue

            shortest[(city, stops)] = price

            for adj_destination_city, adj_price in adj[city]:
                heapq.heappush(minheap, (adj_price + price, adj_destination_city, stops + 1))

        return -1




 
