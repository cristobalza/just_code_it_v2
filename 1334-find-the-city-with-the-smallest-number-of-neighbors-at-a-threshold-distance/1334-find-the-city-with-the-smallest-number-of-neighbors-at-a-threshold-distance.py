class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Custom Djikstra
        # Visit each node and check how may ways we can explore considering the threshold

        from collections import defaultdict

        adj = defaultdict(list) # from: (to, distance)

        for n1, n2, dist in edges:
            adj[n1].append((n2, dist))
            adj[n2].append((n1, dist))

        def dijkstra(src):

            minheap = [(0, src)] # dist, node
            visited = set()

            while minheap:

                dist, node = heapq.heappop(minheap)

                if node in visited:
                    continue
                
                visited.add(node)

                for adj_node, adj_dist in adj[node]:
                    if adj_dist + dist <= distanceThreshold:
                        heapq.heappush(minheap, (adj_dist + dist, adj_node))

            return len(visited) - 1

        # Main
        res, min_count = float("inf"), float("inf")
        for src_node in range(n):
            count = dijkstra(src_node)
            if count <= min_count:
                res = src_node
                min_count = count

        return res


