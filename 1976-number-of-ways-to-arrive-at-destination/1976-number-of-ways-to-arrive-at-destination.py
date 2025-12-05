class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MODULO = (10**9) + 7
        adj = collections.defaultdict(list) # from: (to, weight)
        for n1, n2, weight in roads:
            adj[n1].append((n2, weight))
            adj[n2].append((n1, weight))

        minheap = [] # (weigth, node)
        minheap.append((0, 0))

        dist = [float("inf")] * n
        ways = [0] * n

        dist[0] = 0
        ways[0] = 1

        while minheap:
            weight, node = heapq.heappop(minheap)

            if weight > dist[node]:
                continue

            for adj_node, adj_weight in adj[node]:

                if weight + adj_weight < dist[adj_node]:
                    # Found shorter path
                    dist[adj_node] = weight + adj_weight
                    ways[adj_node] = ways[node]
                    heapq.heappush(minheap, (weight + adj_weight, adj_node))
                elif weight + adj_weight == dist[adj_node]:
                    # Found ANOTHER equivalent path
                    ways[adj_node] = (ways[adj_node] + ways[node]) % MODULO

        return ways[n - 1]


        