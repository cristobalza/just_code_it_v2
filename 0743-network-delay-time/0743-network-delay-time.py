class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Given 
            times: list of u, v, w(time)
                Directed graph
            n: number of nodes
            k: starting node

        Retunr min time takes for all n nodes to receive the signal
            If its impossible return -1

        build the adjacent list for a directed graph
        {
            2 : [(1, 1), (3, 1)]
            3 : [(4, 1)]
            1 : []
            4 : []
        }

        hmap = {1: 1, 2: 0, 3: 1, 4: 2}
        at node= 1, time= 1+ 

            hmap[node] = time

            for adj_node, adj_time in adj[node]:
                dfs(adj_node, adj_time + time)

        res = max()
        """

        adj = {node: [] for node in range(1, n + 1)}
        # Directed graph
        for u, v, w in times:
            adj[u].append((v, w))

        hmap = {node: float('inf') for node in range(1, n + 1)}

        def dfs(node, time):
            # If we've already reached this node with a shorter time, stop
            if time >= hmap[node]:
                return 

            hmap[node] = time

            for adj_node, adj_time in adj[node]:
                dfs(adj_node, adj_time + time)

            return

        dfs(k, 0)

        res = max(hmap.values())

        return res if res != float('inf') else -1
        
        

        
        